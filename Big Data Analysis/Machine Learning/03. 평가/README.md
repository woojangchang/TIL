# 3

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

