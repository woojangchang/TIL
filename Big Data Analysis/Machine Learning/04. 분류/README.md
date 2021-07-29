# 4

- 결정 트리 (의사결정나무)
  - `DecisionTreeClassifier(max_depth, min_samples_split, min_samples_leaf)`
    - `.fit(X_train, y_train)` : 학습
    - `.predict(X_test)` : 예측
    - `.feature_importances_`  : 각 feature의 중요도를 array로 반환
  
- Graphviz
  - `export_graphviz(dt_clf, out_file='tree.dot', class_names=iris_data.target_names, feature_names=iris_data.feature_names, impurity=True, filled=True)`
  
- 가상 데이터 생성
  - `make_classification(n_features=2, n_redundant=0, n_informative=2, n_classes=3, n_clusters_per_class=1, random_state=0)`
    - return `X_features, y_labels`
  
- 앙상블
  - `VotingClassifier(estimators=[('LR', lr_clf), ('KNN', knn_clf)], voting='soft')`
    - `.fit(X_train, y_train)`
    - `.predict(X_test)`
  
- 랜덤 포레스트
  - `RandomForestClassifier()`
    - `n_estimator` : classifier 개수 (default : 100)
    - `n_jobs=-1` : 전체 cpu 콜을 활용
  
- Gradient Boosting Machine
  - `GradientBoostingClassifier()` : weight를 주기 때문에 수행 시간이 꽤 걸림
    - `loss`
    - `n_estimator`
    - `learning_rate`
    - `subsample`
  
- 파이썬 래퍼 XGBoost

  - 설치

    1. Anaconda Prompt 관리자 권한으로 실행

       (설치할 가상환경 활성화)

    2. `conda install -c anaconda py-xgboost`

    3. `import xgboost`, `xgboost.__version__`

    - 또는 `python -m pip install --upgrade xgboost`

  - `import xgboost as xgb`

  - xgboost를 사용하기 위해서 전용 데이터 방식인 DMatrix로 변환해야함

    ```python
    dtrain = xgb.DMatrix(data=X_train, label=y_train)
    dtest = xgb.DMatrix(data=X_test, label=y_test)
    ```

  - `xgb_model = xgb.train(params=params, dtrain=dtrain, num_boost_round=num_rounds, early_stopping_rounds=100, evals=wlist)`

    - `params` : 수많은 하이퍼 파라미터가 있기 때문에 [ipynb 파일](03.%20XGBoost.ipynb) 참고
    - `dtrain` : 학습용 데이터셋
    - `num_boost_round` : 반복 학습 횟수
    - `early_stopping_rounds` : 학습률의 진전이 어느 이상 발전되지 않고 높아지거나 비슷한 것이 n번 지속되면 학습 중단
    - `evals` : 평가용 데이터셋

  - `pred_probs = xgb_model.predict(dtest)`

    - 확률값으로 반환

  - `plot_importance(xgb_model, ax=ax)` : 중요한 feature를 F Score로 시각화

    - `xgb_model` : 학습 완료된 모델
    - `ax=ax` : matplotlib plot

  - `xgb.cv()` : 교차 검증

- 사이킷런 래퍼 XGBoost

  - `from xgboost import XGBClassifier`
  - DMatrix로 변환할 필요 없이 DataFrame이나 numpy array로 사용 가능
  - `xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)`
  - `xgb_wrapper.fit(X_train, y_train, early_stopping_rounds=400, eval_set=evals, eval_metric="logloss", verbose=True)`

- LightGBM

  - 설치
    1. https://visualstudio.microsoft.com/ko/downloads/
    
    2. Visual Studio Build Tools 2019 설치
    
    3. C++ 도구 설치
    
    4. Anaconda Prompt 관리자 권한으로 실행
    
       (설치할 가상환경 활성화)
    
    5. `conda install -c conda-forge lightgbm`
    
  - `lgbm_wrapper = LGBMClassifier(n_estimators=400)`

    - `boost_from_average=False` : 불균형한 데이터셋에서 사용
      - True일 때 재현율과 AUC 성능이 매우 저하됨
      - 일반적인 데이터셋에서는 True를 쓰는 것이 더 좋음

  - `lgbm_wrapper.fit(X_train, y_train, early_stopping_rounds=100, eval_metric='logloss', eval_set=evals, verbose=True)`

- SMOTE

  - 설치

     1. Anaconda Prompt 관리자 권한으로 실행

        (설치할 가상환경 활성화)

    	2. `conda install -c conda-forge imbalanced-learn`

  - `smote.fit_resample(X_train, y_train)`

    - return `X_train_over, y_train_over`

  - 재현율은 높이고 정밀도는 낮춘다.

