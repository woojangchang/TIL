도서 : 파이썬 머신러닝 완벽 가이드

[02. 사이킷런으로 시작하는 머신러닝](02.%20사이킷런으로%20시작하는%20머신러닝)

[03. 평가](03.%20평가)

[04. 분류](04.%20분류)

[05. 회귀](05.%20회귀)

# 머신러닝

알고리즘 관련 패키지 정리

| from                    | import                     | type                   | Chapter |
| ----------------------- | -------------------------- | ---------------------- | ------- |
| sklearn.model_selection | train_test_split           | 데이터셋 분할          | 2       |
| sklearn.model_selection | KFold                      | 교차 검증              | 2       |
| sklearn.model_selection | StratifiedKFold            | 교차 검증              | 2       |
| sklearn.model_selection | cross_val_score            | 교차 검증              | 2       |
| sklearn.model_selection | GridSearchCV               | 최적 하이퍼 파라미터   | 2       |
| sklearn.preprocessing   | LabelEncoder               | 전처리 - 인코딩        | 2       |
| sklearn.preprocessing   | OneHotEncoder              | 전처리 - 인코딩        | 2       |
| sklearn.preprocessing   | StandardScaler             | 전처리 - 피쳐 스케일링 | 2       |
| sklearn.preprocessing   | MinMaxScaler               | 전처리 - 피쳐 스케일링 | 2       |
| sklearn.metrics         | confusion_matrix           | 평가 - 오차 행렬       | 3       |
| sklearn.metrics         | accuracy_score             | 평가 - 오차 행렬       | 2, 3    |
| sklearn.metrics         | precision_score            | 평가 - 오차 행렬       | 3       |
| sklearn.metrics         | recall_score               | 평가 - 오차 행렬       | 3       |
| sklearn.preprocessing   | Binarizer                  | 전처리 - 인코딩        | 3       |
| sklearn.metrics         | precision_recall_curve     | 평가 - 오차 행렬       | 3       |
| sklearn.metrics         | f1_score                   | 평가 - 오차 행렬       | 3       |
| sklearn.metrics         | roc_curve                  | ROC Curve              | 3       |
| sklearn.metrics         | roc_auc_score              | ROC Curve              | 3       |
| sklearn.neighbors       | KNeighborsClassifier       | 분류 - KNN             | 2       |
| sklearn.tree            | DecisionTreeClassifier     | 분류 - 결정 트리       | 4       |
| sklearn.tree            | export_graphviz            | 분류 - 결정 트리       | 4       |
|                         | graphviz                   | 분류 - 결정 트리       | 4       |
| sklearn.linear          | LogisticRegression         | 분류 - 로지스틱        | 3, 4, 5 |
| sklearn.datasets        | make_classification        | 샘플 데이터            | 4       |
| sklearn.ensemble        | VotingClassifier           | 분류 - 앙상블          | 4       |
| sklearn.ensemble        | RandomForestClassifier     | 분류 - 앙상블          | 4       |
| sklearn.ensemble        | GradientBoostingClassifier | 분류 - GBM             | 4       |
|                         | xgboost.DMatrix            | 분류 - GBM             | 4       |
| xgboost                 | XGBClassifier              | 분류 - GBM             | 4       |
| lightgbm                | LGBMClassifier             | 분류 - GBM             | 4       |
| imblearn.over_sampling  | SMOTE                      | 전처리 - 오버 샘플링   | 4       |
| sklearn.linear_model    | LinearRegression           | 회귀 - 선형            | 5       |
| sklearn.metrics         | mean_absolute_error        | 평가 - 회귀            | 5       |
| sklearn.metrics         | mean_squared_error         | 평가 - 회귀            | 5       |
| sklearn.metrics         | r2_score                   | 평가 - 회귀            | 5       |
| sklearn.preprocessing   | PolynomialFeatures         | 전처리 - 다항 회귀     | 5       |
| sklearn.pipeline        | Pipeline                   | 파이프라인             | 5       |
| sklearn.linear_model    | Ridge                      | 회귀 - 선형            | 5       |
| sklearn.linear_model    | Lasso                      | 회귀 - 선형            | 5       |
| sklearn.linear_model    | ElasticNet                 | 회귀 -선형             | 5       |
| sklearn.tree            | DecisionTreeRegressor      | 회귀 - 트리            | 5       |
| sklearn.ensemble        | GradientBoostingRegressor  | 회귀 - 트리            | 5       |
| xgboost                 | XGBRegressor               | 회귀 - 트리            | 5       |
| lightgbm                | LGBMRegressor              | 회귀 - 트리            | 5       |

