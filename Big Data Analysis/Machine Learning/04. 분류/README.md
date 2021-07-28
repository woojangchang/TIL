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

