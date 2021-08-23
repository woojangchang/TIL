# 자주 사용하는 라이브러리

## 통계

| from                    | import            | 용도                                                   |
| ----------------------- | ----------------- | ------------------------------------------------------ |
| sklearn.linear_model    | LinearRegression  | 회귀 계수 파악                                         |
| statsmodels.api         | OLS, add_constant | 회귀 계수 파악<br />p-value 확인                       |
| statsmodels.formula.api | ols               | 회귀 계수 파악<br />p-value 확인                       |
| pandas                  | crosstab          | 범주형 변수의 빈도/합/평균 등 확인                     |
| pandas                  | pivot_table       | 범주형 변수의 빈도/합/평균 등 확인                     |
| scipy.stats             | ch2_contingency   | 범주형 변수의 독립성 검정<br />빈도 테이블을 입력 받음 |
| scipy.stats             | ttest_ind         | 독립 표본 t 검정                                       |
| scipy.stats             | ttest_rel         | 대응 표본 t 검정                                       |
|                         |                   |                                                        |



## 머신러닝

| from                 | import                 | 용도                                        |
| -------------------- | ---------------------- | ------------------------------------------- |
| sklearn.tree         | DecisionTreeClassifier | 결정 나무(분류)                             |
| sklearn.tree         | plot_tree              | 이미지로 트리 확인<br />Root Node 확인 용도 |
| sklearn.tree         | export_text            | 텍스트로 트리 확인<br />Root Node 확인 용도 |
| sklearn.linear_model | LogisticRegression     | 로지스틱 분류                               |
| sklearn.metrics      | classification_report  | 분류 평가 지표 확인                         |

