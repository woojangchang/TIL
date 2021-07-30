# 5

- 선형 회귀
  - `LinearRegression()`
    - `fit_intercept=True` : 절편 계산
    - `normalize=False` : 정규화
    - `.coef_` : 회귀계수
    - `.intercept_` : 절편
- scoring 파라미터
  - `neg_mean_squared_error`
- 다항 회귀 변환
  - `PolynomialFeatures(degree=3)`
    - `degree` : 차항
  - `Pipeline([('poly', PolynomialFeatures(degree=3)), ('linear', LinearRegression())])`
- 릿지 회귀
  - `Ridge(alpha)`
- 로지스틱 회귀
  - `LogisticRegression(penalty='l2', C=1.0)`
    - `penalty` : 규제 유형으로 'l1', 'l2', 'elasticnet'이 있음
    - `C` : 규제 강도 조절 alpha의 역수, C값이 작을수록 규제 강함
- 회귀 트리
  - `RandomForestRegressor()`
  - `DecisionTreeRegressor()`
  - `GradientBoostingRegressor()`
  - `XGBRegressor()`
  - `LGBMRegressor()`

