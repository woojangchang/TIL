도서 : 파이썬 머신러닝 완벽 가이드

[02. 사이킷런으로 시작하는 머신러닝](02.%20사이킷런으로%20시작하는%20머신러닝)

[03. 평가](03.%20평가)

# 머신러닝

## 2

- scikit-learn
  - `.fit(X, y)`, `.score()`, `.predict(X_test)`
  - `train_test_split(X, y, test_size=0.25, stratify=True)`
    - return `X_train, X_test, y_train, y_test`
  
- numpy
  - `.shuffle()`, `.column_stack()`, `.concatenate()`

- 데이터 세트 준비 > 모델 학습 > 예측 수행 > 모델 성능 평가

- 교차 검증
  - `KFold(n_splits=5)`

  ```python
  kfold = KFold()
  for train_idx, text_idx in kfold.split(X):
      X_train, X_test = X[train_idx], X[test_idx]
      y_train, y_test = y[train_idx], y[test_idx]
  ```

  - `StratifiedKFold(n_splits=5)`

  ```python
  skf = StratifiedKFold()
  for train_idx, text_idx in skf.split(X):
      X_train, X_test = X[train_idx], X[test_idx]
      y_train, y_test = y[train_idx], y[test_idx]
  ```

  - `cross_val_score(estimator, X, y, cv=5)`
    - `cv` : fold 개수
    - return `scores` (교차 검증한 정확도 리스트 반환)

- 하이퍼 파라미터
  - `GridSearchCV(estimator, param_grid, scoring='accuracy', cv=5)`
    - `.cv_results_` : 결과 array 반환 (pandas DataFrame으로 눈에 보기 편한 형태로 가능)
    -  `.best_params_` : best score가 나온 parameter
    - `.best_score_`
    - `.best_estimator_` : best score가 나온 학습된 estimator
  
- 레이블 인코딩
  - `LabelEncoder()`
    - `.fit(X)`, `.transform(X)` : 학습, 변환
    - `.classes_` : encode 전 classes
    - `.inverse_transform()` : decode
  
- 원-핫 인코딩
  - `OneHotEncoder()`
    - `.toarray()` : 압축되어 있는 결과를 array로
  - Pandas
    - `.get_dummies()` : pandas 원-핫 인코딩
    - `.to_numpy()`

## 3

- 정확도
  - `accuracy_score(y_test, pred)`
  
- 오차행렬
  - `confusion_matrix(y_test, pred)`

    - ```python
      # 아래와 같은 결과가 나온다.
      '''
      array([[ TN,   FP],
             [ FN,   TP]], dtype=int64)
      '''
      ```

- 정밀도
  - `precision_score(y_test, pred)`
  
- 재현율
  - `recall_score(y_test, pred)`
  
- `LogisticRegression()`

  - `.predict(X_train)`
    - 0과 1로 이루어진 array 반환
  - `.predict_proba(X_train)`
    - 0번째 열에는 0일 확률, 1번째 열에는 1일 확률인 array 반환

- F1 Score
  - `f1_score(y_test, pred)`
  
- G Measure

- ROC Curve
  - `roc_curve(y_test, pred_proba)`
    - return `fprs, tprs, thresholds`
  - `roc_auc_score(y_test, pred_proba)`


