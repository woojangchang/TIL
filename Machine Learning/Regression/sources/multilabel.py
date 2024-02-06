import numpy as np
import pandas as pd
import joblib
import os
from scipy.stats import pearsonr
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor


class MultilabelPredictor:
    """
    labels: y인자 컬럼명
    eval_metrics: list or str
        XGBoost: {"reg:squarederror", "reg:absoluteerror"}, default:"reg:squarederror" (objective)
        RandomForest: {"squared_error", "absolute_error"}, default:"squared_error" (criterion)
        LightGBM: default:None
    consider_labels_correlation: default:True
        lables=[l1, l2, l3]일 때
        l1의 학습 features = l1, l2, l3를 제외한 모든 features
        l2의 학습 features = l2, l3를 제외한 모든 features (l1 포함)
        l3의 학습 features = l3를 제외한 모든 features (l1, l2 포함)
    model: {"XGBoost", "RandomForest", "LightGBM"}, default:"XGBoost"
    params: parameters of model
    """
    
    def __init__(self, labels, eval_metrics=None, consider_labels_correlation=True, model='XGBoost', **params):
        if len(labels) < 2:
            raise ValueError("MultilabelPredictor is only intended for predicting MULTIPLE labels (columns).")
        if (eval_metrics is not None) and (len(eval_metrics) != len(labels)):
            raise ValueError("If provided, `eval_metrics` must have same length as `labels`")
        self.labels = labels
        self.consider_labels_correlation = consider_labels_correlation
        self.predictors = {}  # key = label, value = model
        self.feature_names = {}
        self.model = model
        
        if eval_metrics is None and model=='XGBoost':
            self.eval_metrics = {labels[i] : 'reg:squarederror' for i in range(len(labels))}
        elif eval_metrics is None and model=='RandomForest':
            self.eval_metrics = {labels[i] : 'squared_error' for i in range(len(labels))}
        elif eval_metrics is None and model=='LightGBM':
            self.eval_metrics = {labels[i] : None for i in range(len(labels))}
        elif isinstance(eval_metrics, list):
            self.eval_metrics = {labels[i] : eval_metrics[i] for i in range(len(labels))}
        elif isinstance(eval_metrics, dict):
            self.eval_metrics = {label: eval_metrics[label] for label in labels}
            
        for label in labels:
            if self.model == 'XGBoost':
                self.predictors[label] = XGBRegressor(objective=self.eval_metrics[label], **params)
            elif self.model == 'RandomForest':
                self.predictors[label] = RandomForestRegressor(criterion=self.eval_metrics[label], **params)
            elif self.model == 'LightGBM':
                self.predictors[label] = LGBMRegressor(objective=self.eval_metrics[label], **params)
                
            

    def fit(self, train_data, **kwargs):
        """
        train_data: pandas DataFrame
        **kwargs: keyword arguments of predictor.fit()
        """
        
        train_data_og = train_data.copy()
        for i in range(len(self.labels)):
            label = self.labels[i]
            predictor = self.predictors[label]
            if not self.consider_labels_correlation:
                labels_to_drop = [l for l in self.labels if l != label]
            else:
                labels_to_drop = [self.labels[j] for j in range(i+1, len(self.labels))]
            
            train_data = train_data_og.drop(columns=labels_to_drop)
            
            X = train_data.drop(columns=label)
            y = train_data[label]
            predictor.fit(X.values, y.values, **kwargs)
            
            self.predictors[label] = predictor
            self.feature_names[label] = X.columns.tolist()
                        
        return self
            

    def predict(self, data, **kwargs):
        """
        data: pandas DataFrame
        **kwargs: keyword arguments of predictor.predict()
        """
        X_test = data.copy()
        
        result = pd.DataFrame()
        for label in self.labels:
            predictor = self.predictors[label]
            feature_names = self.feature_names[label]
            pred = predictor.predict(X_test[feature_names].values, **kwargs)
            result[label] = pred
            if self.consider_labels_correlation:
                X_test[label] = pred
            
        result.index = data.index
        
        return result


    def evaluate(self, data, **kwargs):
        """
        data: pandas DataFrame
        **kwargs: keyword arguments of predictor.predict()
        """
        eval_dict = {}
        
        preds = self.predict(data, **kwargs)
        for label in self.labels:
            pred = preds[label]
            real = data[label]
            
            mae = mean_absolute_error(real, pred)
            rmse = np.sqrt(mean_squared_error(real, pred))
            r2 = r2_score(real, pred)
            pearson_corr, _ = pearsonr(real, pred)
            mape = mean_absolute_percentage_error(real, pred)
        
            eval_dict[label] = {'mae':mae, 'rmse':rmse, 'mape': mape, 'r2':r2, 'pearsonr':pearson_corr}
            
        return pd.DataFrame(eval_dict)

    
    def save(self, path):
        """
        path: 모델 저장 경로 지정
        """
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)

        # 모델 구성 저장
        config = {}
        
        config['model'] = self.model
        config['eval_metrics'] = self.eval_metrics
        config['consider_labels_correlation'] = self.consider_labels_correlation
        config['labels'] = self.labels
        config['feature_names'] = self.feature_names
        config_path = os.path.join(path, 'config.json')
        with open(config_path, 'w', encoding='utf-8-sig') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)

        # 모든 모델 저장
        for label, predictor in self.predictors.items():
            model_path = os.path.join(path, f'{label}.joblib')
            joblib.dump(predictor, model_path)

    @classmethod
    def load(cls, path):
        """
        path: 저장된 모델 경로 지정
        """
        config_path = os.path.join(path, 'config.json')
        with open(config_path, 'r', encoding='utf-8-sig') as f:
            config = json.load(f)
        
        # 새 인스턴스 생성
        model_type = config.pop('model', 'XGBoost') 
        eval_metrics = config.pop('eval_metrics', None)
        instance = cls(labels=config['labels'], eval_metrics=eval_metrics,
                       consider_labels_correlation=config['consider_labels_correlation'], model=model_type)

        # 명시적으로 속성을 업데이트
        for key, value in config.items():
            setattr(instance, key, value)

        # 모든 모델을 로드하여 인스턴스에 설정
        instance.predictors = {}
        for label in instance.labels:
            model_path = os.path.join(path, f'{label}.joblib')
            instance.predictors[label] = joblib.load(model_path)

        return instance