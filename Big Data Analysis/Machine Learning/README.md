도서 : 파이썬 머신러닝 완벽 가이드

[02. 사이킷런으로 시작하는 머신러닝](02.%20사이킷런으로%20시작하는%20머신러닝)

# 머신러닝

## 02. 사이킷런으로 시작하는 머신러닝

### 01. 머신러닝 개요

- K-Nearest Neighbor Algorithm
- scikit-learn
  - `.fit()`, `.score()`, `.predict()`
  - `train_test_split()`, `stratify=`
- numpy
  - `.shuffle()`, `.column_stack()`, `.concatenate()`

### 02. 붓꽃 품종 분류

- 데이터 세트 준비 > 모델 학습 > 예측 수행 > 모델 성능 평가

### 03. 프레임워크

### 04. Model Selection

- 홀드 아웃
- 교차 검증
  - `KFold`, `n_splits=`
  - `cross_val_score()`
- 하이퍼 파라미터
  - `GridSearchCV`
    - `.cv_results_`, `.best_params_`, `.best_score_`, `.best_estimator_`

### 05. 데이터 전처리

- 레이블 인코딩
  - `LabelEncoder`, `.fit()`, `.transform()`
  - `.classes_`, `.inverse_transform()`
- 원-핫 인코딩
  - `OneHotEncoder`
  - Pandas
    - `.get_dummies()`, .`to_numpy()`

### 06. 타이타닉 생존자 예측

- `.fillna()`

