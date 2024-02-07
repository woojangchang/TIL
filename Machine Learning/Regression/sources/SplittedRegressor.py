import numpy as np
import pandas as pd


def make_dataset(df, label, center, alpha):
    """
    데이터 분류 후 회귀 예측을 하는 모델 생성을 위한 데이터 초기화
    
    Parameters
    ----------
    df: X, y가 모두 포함된 dataframe
    label: y의 컬럼명
    center, alpha: center 기준 +-alpha로 데이터셋 생성
        alpha가 0인 경우 center보다 크면 True, 아니면 False
    
    
    Returns
    -------
    df_clf_left_, df_clf_right_, df_reg_left_, df_reg_right_
    
    alpha > 0인 경우
        y <= center+alpha인지 예측하는 분류 모델을 위한 데이터셋,
        y > center-alpha인지 예측하는 분류 모델을 위한 데이터셋,
        y <= center+alpha에서 예측하는 회귀 모델을 위한 데이터셋,
        y < center-alpha에서 예측하는 회귀 모델을 위한 데이터셋 순
        
    alpha = 0인 경우
        y < center인지 예측하는 분류 모델을 위한 데이터셋,
        None,
        y <= center+alpha에서 예측하는 회귀 모델을 위한 데이터셋,
        y < center-alpha에서 예측하는 회귀 모델을 위한 데이터셋 순
    
    """
    assert alpha >= 0, f"alpha >= 0 (input: {alpha})"
    
    if alpha != 0:
        df_clf_right_ = df.copy()
        df_clf_left_ = df.copy()
        df_reg_right_ = df.copy()
        df_reg_left_ = df.copy()

        y_left_ = df[label] <= center+alpha
        y_right_ = df[label] > center-alpha

        df_clf_right_[label] = y_right_
        df_clf_left_[label] = y_left_

        df_reg_right_ = df_reg_right_[y_right_]
        df_reg_left_ = df_reg_left_[y_left_]

        return df_clf_left_, df_clf_right_, df_reg_left_, df_reg_right_
    
    else:
        df_clf_ = df.copy()
        df_reg_right_ = df.copy()
        df_reg_left_ = df.copy()

        y_left_ = df[label] <= center
        y_right_ = df[label] > center

        df_clf_[label] = y_right_

        df_reg_right_ = df_reg_right_[y_right_]
        df_reg_left_ = df_reg_left_[y_left_]

        return df_clf_, None, df_reg_left_, df_reg_right_
    

    
class SplittedRegressor1:
    """
    두 개의 분포로 이루어진 Y를 예측하는 데 두 분포 중 어디에 속하는 지 분류한 후 Y를 예측하는 모델.
    중첩되는 부분까지 고려하여 두 개의 분류 모델과 두 개의 회귀 모델로 이루어짐.
    """
    
    def __init__(self, label, clf_left, clf_right, reg_left, reg_right):
        """
        label: y 컬럼명
        clf_left, clf_right: 왼쪽, 오른쪽 분류 모델
        reg_left, reg_right: 왼쪽, 오른쪽 회귀 모델
        """
        self.label = label
        self.clf_left = clf_left
        self.clf_right = clf_right
        self.reg_left = reg_left
        self.reg_right = reg_right
        
    
        
        
    def fit(self, train_data:pd.DataFrame, center, alpha):
        """
        Parameters
        ----------
        train_data: y가 포함된 학습 데이터. 
        center, alpha: float, float.
                       Y <= center+alpha, Y > center-alpha 두 가지 예측 모델 생성.                    
        
        """
        assert alpha > 0, "alpha > 0"
        
        # 학습 데이터 초기화
        df_train_clf_left, df_train_clf_right, \
        df_train_reg_left, df_train_reg_right = make_dataset(train_data, self.label, center, alpha)
        
                
        # 학습
        self.clf_left.fit(df_train_clf_left.drop(columns=self.label), df_train_clf_left[self.label])
        self.clf_right.fit(df_train_clf_right.drop(columns=self.label), df_train_clf_right[self.label])
        
        self.reg_left.fit(df_train_reg_left.drop(columns=self.label), df_train_reg_left[self.label])
        self.reg_right.fit(df_train_reg_right.drop(columns=self.label), df_train_reg_right[self.label])
        
        return self
        
        
    def predict(self, X:pd.DataFrame):
        """
        Parameters
        ----------
        X: 테스트 데이터.
        
        
        Returns
        -------
        pred: pd.Series. 예측값
        """
        
        # 결과 데이터 초기화
        pred = pd.Series([0 for _ in range(len(X))], name=self.label, index=X.index)
        
#         print('예측값 초기화 완료')
        
        # 왼쪽/오른쪽 구간 분류
        # 두 개의 분류 모델이 서로 같은 결과를 내놓을 경우
        is_left = self.clf_left.predict_proba(X)[:, 0] # 왼쪽 모델의 왼쪽에 대한 확률값
        is_right = self.clf_right.predict_proba(X)[:, 0] # 오른쪽 모델의 오른쪽에 대한 확률값
        
#         print('분류 모델 예측 완료')
        
        left_index = (is_left >= 0.5) & (is_right < 0.5)
        right_index = (is_left < 0.5) & (is_right >= 0.5)
        
        # 왼쪽/오른쪽 각각 예측
        if left_index.sum() > 0:
            left = self.reg_left.predict(X[left_index])
            pred[left_index] = left
            
        if right_index.sum() > 0:
            right = self.reg_right.predict(X[right_index])
            pred[right_index] = right


#         print('예측값 업데이트 완료')
        
        # 두 개의 분류 모델의 예측 결과가 서로 다른 경우
        # 각각의 회귀 모델 예측값의 가중 평균으로 대체, 가중치는 예측 확률값
        case1_index = (is_left >= 0.5) & (is_right >= 0.5) # 왼쪽 모델은 왼쪽, 오른쪽 모델은 오른쪽에 있다고 예측한 경우
        if len(case1_index) > 0:
            case1_left = self.reg_left.predict(X[case1_index])
            case1_right = self.reg_right.predict(X[case1_index])
            case1_left_weight = is_left[case1_index]
            case1_right_weight = is_right[case1_index]
            pred[case1_index] = (case1_left * case1_left_weight + case1_right * case1_right_weight) / (case1_left_weight + case1_right_weight)
        
#             print('회귀 모델 Case 1 예측 완료')
        
        case2_index = (is_left < 0.5) & (is_right < 0.5) # 왼쪽 모델은 오른쪽, 오른쪽 모델은 왼쪽에 있다고 예측한 경우
        if len(case2_index) > 0:
            case2_left = self.reg_left.predict(X[case2_index])
            case2_right = self.reg_right.predict(X[case2_index])
            case2_right_weight = is_left[case2_index]
            case2_left_weight = is_right[case2_index]
            pred[case2_index] = (case2_left * case2_left_weight + case2_right * case2_right_weight) / (case2_left_weight + case2_right_weight)

#             print('회귀 모델 Case 2 예측 완료')
        
        return pred
    
    def evaluate(self, X, y):
        """
        Parameters
        ----------
        X, y: 평가 데이터
        
        
        Returns
        -------
        eval_metrics: pd.DataFrame. RMSE, MAE, R Square, 상관계수
        
        """
        
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        from scipy.stats import pearsonr
        
        pred = self.predict(X)
        
        mae = mean_absolute_error(y, pred)
        rmse = np.sqrt(mean_squared_error(y, pred))
        r2 = r2_score(y, pred)
        pearson_corr, _ = pearsonr(y, pred)
        
        result = {'root_mean_squared_error':rmse, 'mean_absolute_error':mae, 'r2':r2, 'pearsonr':pearson_corr}
        
        eval_metrics = pd.DataFrame([result]).T
        
        return eval_metrics

    
    
    
class SplittedRegressor2:
    """
    두 개의 분포로 이루어진 Y를 예측하는 데 두 분포 중 어디에 속하는 지 분류한 후 Y를 예측하는 모델.
    하나의 분류 모델과 두 개의 회귀 모델로 이루어짐.
    """
    
    def __init__(self, label, clf, reg_left, reg_right):
        self.label = label
        self.clf = clf
        self.reg_left = reg_left
        self.reg_right = reg_right
        
        
    def fit(self, train_data, center):
        """
        Parameters
        ----------
        train_data: pandas.DataFrame. 학습 데이터. 
        center: float. Y <= center, Y > center 두 가지 예측 모델 생성.
        """        
        # 학습 데이터 초기화
        df_train_clf, _, df_train_reg_left, df_train_reg_right = make_dataset(train_data, self.label, center, 0)
        
                
        # 학습
        self.clf.fit(df_train_clf.drop(columns=self.label), df_train_clf[self.label])
        
        self.reg_left.fit(df_train_reg_left.drop(columns=self.label), df_train_reg_left[self.label])
        self.reg_right.fit(df_train_reg_right.drop(columns=self.label), df_train_reg_right[self.label])

        return self
        
        
    def predict(self, X, alpha_prob=0.1):
        """
        Parameters
        ----------
        X: pd.DataFrame. 테스트 데이터.
        alpha_prob: 확률이 차이가 alpha_prob 이하인 경우 가중 평균
            ex) 오른쪽 구간에 속할 확률이 0.55인 경우 (왼쪽 구간은 0.45이므로 alpha_prob=0.1 이하)
                오른쪽 회귀 예측값 * 0.55 + 왼쪽 회귀 예측값 * 0.45
        
        Returns
        -------
        pred: pd.Series. 예측값
        """
        
        # 결과 데이터 초기화
        pred = pd.Series([0 for _ in range(len(X))], name=self.label, index=X.index)
        
#         print('예측값 초기화 완료')
        
        # 왼쪽/오른쪽 구간 분류
        # 확률의 차이가 alpha_prob보다 큰 경우
        is_left = self.clf.predict_proba(X)[:, 0] # 왼쪽일 확률
        
#         print('분류 모델 예측 완료')
        
        
        left_index = is_left >= 0.5 + alpha_prob / 2
        right_index = is_left < 0.5 - alpha_prob / 2
        
        # 왼쪽/오른쪽 각각 예측
        if left_index.sum() > 0:
            left = self.reg_left.predict(X[left_index])
            pred[left_index] = left
        if right_index.sum() > 0:
            right = self.reg_right.predict(X[right_index])
            pred[right_index] = right


#         print('예측값 업데이트 완료')
        
        # 확률의 차이가 alpha_prob 이하일 경우
        # 각각의 회귀 모델 예측값의 가중 평균으로 대체
        case_index = (is_left < 0.5 + alpha_prob / 2) & (is_left >= 0.5 - alpha_prob / 2)
        if len(case_index) > 0:
            case_left = self.reg_left.predict(X[case_index])
            case_right = self.reg_right.predict(X[case_index])
            case_left_weight = is_left[case_index]
            case_right_weight = 1-is_left[case_index]
            pred[case_index] = (case_left * case_left_weight + case_right * case_right_weight)
        
#             print('회귀 모델 Case 1 예측 완료')

        return pred
    
    def evaluate(self, X, y, alpha_prob=0.1):
        """
        Parameters
        ----------
        X, y: 테스트 데이터
        alpha_prob: 확률이 차이가 alpha_prob 이하인 경우 가중 평균
            ex) 오른쪽 구간에 속할 확률이 0.55인 경우 (왼쪽 구간은 0.45이므로 alpha_prob=0.1 이하)
                오른쪽 회귀 예측값 * 0.55 + 왼쪽 회귀 예측값 * 0.45
        
        Returns
        -------
        eval_metrics: pd.DataFrame. RMSE, MAE, R Square, 상관계수
        
        """
        
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        from scipy.stats import pearsonr
        
        pred = self.predict(X, alpha_prob)
        
        mae = mean_absolute_error(y, pred)
        rmse = np.sqrt(mean_squared_error(y, pred))
        r2 = r2_score(y, pred)
        pearson_corr, _ = pearsonr(y, pred)
        
        result = {'root_mean_squared_error':rmse, 'mean_absolute_error':mae, 'r2':r2, 'pearsonr':pearson_corr}
        
        eval_metrics = pd.DataFrame([result]).T
        
        return eval_metrics
