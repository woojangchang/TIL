도서 : 파이썬 머신러닝 완벽 가이드

[02. 사이킷런으로 시작하는 머신러닝](02.%20사이킷런으로%20시작하는%20머신러닝)

[03. 평가](03.%20평가)

[04. 분류](04.%20분류)

[05. 회귀](05.%20회귀)

[06. 차원 축소](06.%20차원%20축소)

[07. 군집화](07.%20군집화)

[08. 텍스트 분석](08.%20텍스트%20분석)

# 머신러닝

알고리즘 관련 패키지 정리

| from                            | import                     | type                        | Chapter |
| ------------------------------- | -------------------------- | --------------------------- | ------- |
| sklearn.model_selection         | train_test_split           | 데이터셋 분할               | 2       |
| sklearn.model_selection         | KFold                      | 교차 검증                   | 2       |
| sklearn.model_selection         | StratifiedKFold            | 교차 검증                   | 2       |
| sklearn.model_selection         | cross_val_score            | 교차 검증                   | 2       |
| sklearn.model_selection         | GridSearchCV               | 최적 하이퍼 파라미터        | 2       |
| sklearn.preprocessing           | LabelEncoder               | 전처리 - 인코딩             | 2       |
| sklearn.preprocessing           | OneHotEncoder              | 전처리 - 인코딩             | 2       |
| sklearn.preprocessing           | LabelBinarizer             | 전처리 - 인코딩 - 희소 행렬 | 8       |
| scipy.sparse                    | hstack                     | 전처리 - 희소 행렬 합치기   | 8       |
| gc                              | collect                    | 메모리 정리                 | 8       |
|                                 | pandas<br />.get_dummies() | 전처리 - 인코딩             | 2       |
| sklearn.preprocessing           | StandardScaler             | 전처리 - 피쳐 스케일링      | 2       |
| sklearn.preprocessing           | MinMaxScaler               | 전처리 - 피쳐 스케일링      | 2       |
| numpy                           | log1p                      | 전처리 - 피쳐 스케일링      | 5, 7    |
| sklearn.metrics                 | confusion_matrix           | 평가 - 오차 행렬            | 3       |
| sklearn.metrics                 | accuracy_score             | 평가 - 오차 행렬            | 2, 3    |
| sklearn.metrics                 | precision_score            | 평가 - 오차 행렬            | 3       |
| sklearn.metrics                 | recall_score               | 평가 - 오차 행렬            | 3       |
| sklearn.preprocessing           | Binarizer                  | 전처리 - 인코딩             | 3       |
| sklearn.metrics                 | precision_recall_curve     | 평가 - 오차 행렬            | 3       |
| sklearn.metrics                 | f1_score                   | 평가 - 오차 행렬            | 3       |
| sklearn.metrics                 | roc_curve                  | ROC Curve                   | 3       |
| sklearn.metrics                 | roc_auc_score              | ROC Curve                   | 3       |
| sklearn.neighbors               | KNeighborsClassifier       | 분류 - KNN                  | 2       |
| sklearn.tree                    | DecisionTreeClassifier     | 분류 - 결정 트리            | 4       |
| sklearn.tree                    | export_graphviz            | 분류 - 결정 트리            | 4       |
|                                 | graphviz                   | 분류 - 결정 트리            | 4       |
| sklearn.linear                  | LogisticRegression         | 분류 - 로지스틱             | 3, 4, 5 |
| sklearn.datasets                | make_classification        | 샘플 데이터                 | 4       |
| sklearn.ensemble                | VotingClassifier           | 분류 - 앙상블               | 4       |
| sklearn.ensemble                | RandomForestClassifier     | 분류 - 앙상블               | 4       |
| sklearn.ensemble                | GradientBoostingClassifier | 분류 - GBM                  | 4       |
|                                 | xgboost.DMatrix            | 분류 - GBM                  | 4       |
| xgboost                         | XGBClassifier              | 분류 - GBM                  | 4       |
| lightgbm                        | LGBMClassifier             | 분류 - GBM                  | 4       |
| imblearn.over_sampling          | SMOTE                      | 전처리 - 오버 샘플링        | 4       |
| sklearn.linear_model            | LinearRegression           | 회귀 - 선형                 | 5       |
| sklearn.metrics                 | mean_absolute_error        | 평가 - 회귀                 | 5       |
| sklearn.metrics                 | mean_squared_error         | 평가 - 회귀                 | 5       |
| sklearn.metrics                 | r2_score                   | 평가 - 회귀                 | 5       |
| sklearn.preprocessing           | PolynomialFeatures         | 전처리 - 다항 회귀          | 5       |
| sklearn.pipeline                | Pipeline                   | 파이프라인                  | 5       |
| sklearn.linear_model            | Ridge                      | 회귀 - 선형                 | 5       |
| sklearn.linear_model            | Lasso                      | 회귀 - 선형                 | 5       |
| sklearn.linear_model            | ElasticNet                 | 회귀 - 선형                 | 5       |
| sklearn.tree                    | DecisionTreeRegressor      | 회귀 - 트리                 | 5       |
| sklearn.ensemble                | GradientBoostingRegressor  | 회귀 - 트리                 | 5       |
| xgboost                         | XGBRegressor               | 회귀 - 트리                 | 5       |
| lightgbm                        | LGBMRegressor              | 회귀 - 트리                 | 5       |
| sklearn.decomposition           | PCA                        | 차원 축소                   | 6       |
| sklearn.discriminant_analysis   | LinearDiscriminantAnalysis | 차원 축소                   | 6       |
| numpy.linalg                    | svd                        | 차원 축소                   | 6       |
| scipy.sparse.linalg             | svds                       | 차원 축소                   | 6       |
| scipy.linalg                    | svd                        | 차원 축소                   | 6       |
| sklearn.decomposition           | TruncatedSVD               | 차원 축소                   | 6       |
| sklearn.decomposition           | NMF                        | 차원 축소                   | 6       |
| sklearn.cluster                 | KMeans                     | 군집화 - K평균              | 7       |
| sklearn.metrics                 | silhouette_samples         | 평가 - 군집화               | 7       |
| sklearn.metrics                 | silhouette_score           | 평가 - 군집화               | 7       |
| sklearn.cluster                 | KMeans<br />.inertia_      | 평가 - 군집화               | 7       |
| sklearn.cluster                 | MeanShift                  | 군집화 - 평균이동           | 7       |
| sklearn.cluster                 | estimate_bandwidth         | 군집화 - 평균이동 최적화    | 7       |
| sklearn.mixture                 | GaussianMixture            | 군집화 - GMM                | 7       |
| sklearn.cluster                 | DBSCAN                     | 군집화 - DBSCAN             | 7       |
| nltk                            | sent_tokenize              | 텍스트 분석 - 문장 토큰화   | 8       |
| nltk                            | word_tokenize              | 텍스트 분석 - 단어 토큰화   | 8       |
| nltk.stem                       | LancasterStemmer           | 텍스트 분석 - 원형 찾기     | 8       |
| nltk.stem                       | WordNetLemmatizer          | 텍스트 분석 - 원형 찾기     | 8       |
| sklearn.feature_extraction.text | CountVectorizer            | 텍스트 분석 - 피처 벡터화   | 8       |
| sklearn.feature_extraction.text | TfidfVectorizer            | 텍스트 분석 - 피처 벡터화   | 8       |
| nltk.corpus                     | sentiwordnet               | 텍스트 분석 - 감성 분석     | 8       |
| nltk                            | pos_tag                    | 텍스트 분석 - 품사          | 8       |
| nltk.sentiment.vader            | SentimentIntensityAnalyzer | 텍스트 분석 - 감성 분석     | 8       |
| pattern.en                      | sentiment                  | 텍스트 분석 - 감성 분석     | 8       |
| sklearn.decomposition           | LatentDirichletallocation  | 텍스트 분석 - 토픽 모델링   | 8       |
| sklearn.metrics.pariwise        | cosine_similarity          | 텍스트 분석 - 문서 유사도   | 8       |
| konlpy.tag                      | Okt                        | 텍스트 분석 - 한글 토큰화   | 8       |

