# 2

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
    - `.fit(X_train, y_train)` : 학습
    - `.cv_results_` : 결과 array 반환 (pandas DataFrame으로 눈에 보기 편한 형태로 가능)
    - `.best_params_` : best score가 나온 parameter
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

