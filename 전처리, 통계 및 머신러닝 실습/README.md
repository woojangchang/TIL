# 자주 사용하는 라이브러리

## 통계

| from                        | import            | 용도                                                         |
| --------------------------- | ----------------- | ------------------------------------------------------------ |
| sklearn.linear_model        | LinearRegression  | 회귀 계수 파악                                               |
| statsmodels.api             | OLS, add_constant | 회귀 계수 파악<br />p-value 확인                             |
| statsmodels.formula.api     | ols               | 회귀, anova 분석<br />p-value 확인                           |
| pandas                      | crosstab          | 범주형 변수의 빈도/합/평균 등 확인                           |
| pandas                      | pivot_table       | 범주형 변수의 빈도/합/평균 등 확인                           |
| scipy.stats                 | ch2_contingency   | 범주형 변수의 독립성 검정<br />빈도 테이블을 입력 받음       |
| scipy.stats                 | ttest_ind         | 독립 표본 t 검정                                             |
| scipy.stats                 | ttest_rel         | 대응 표본 t 검정                                             |
| statsmodels.stats.anova     | anova_lm          | anova 분석                                                   |
| statsmodels.stats.multicomp | pairwise_tukeyhsd | anova 분석                                                   |
| scipy.stats                 | f_oneway          | anova 분석                                                   |
| pandas                      | to_datetime       | 전처리<br />pd.to_datetime(column).dt.year<br />pd.to_datetime(column).dt.month<br />pd.to_datetime(column).dt.day<br />pd.to_datetime(column).dt.day_name() |

### 회귀

#### `sklearn.linear_model.LinearRegression`

```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)
# 회귀계수
lr.coef_

# R2 score
lr.score(X, y)
```

#### `statsmodels.api.OLS`

```python
from statsmodels.api import OLS, add_constant

regg = OLS(y, add_constant(X)).fit() # 절편 추가
regg.summary()
```

#### `statsmodels.formula.api.ols`

```python
from statsmodels.formula.api import ols

formula = '종속변수 ~ 독립변수1 + 독립변수2 + ...'
regg = ols(formula, DataFrame).fit()
regg.summary()
```

### t-test

#### 독립 표본 (ind)

```python
from scipy.stats import ttest_ind

t, p = ttest_ind(x1, x2, equal_var=True) # 동분산일 경우
t, p = ttest_ind(x1, x2, equal_var=False) # 동분산이 아닐 경우
```

#### 대응 표본 (rel)

```python
from scipy.stats import ttest_rel

t, p = ttest_rel(x1, x2)
```

### ANOVA

#### `statsmodels.stats.anova.anova_lm`

```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# C(수치형 변수) : 범주형으로 인식
formula = '비교할 값 ~ C(카테고리 변수명)'
anova = ols(formula, DataFrame).fit()
anova_lm(anova)
```

- DataFrame

| 비교할 값(Price 등) | 카테고리 변수명(year 등) |
| ------------------- | ------------------------ |
| 15                  | 2010                     |
| 4                   | 2010                     |
| 2                   | 2011                     |
| 7                   | 2012                     |
| 13                  | 2013                     |
| ...                 | ...                      |

#### `scipy.stats.f_oneway`

```python
from scipy.stats import f_oneway

f, p = f_oneway(c1, c2, c3, ...)
```

### 독립성 검정

#### `scipy.stats.chi2_contingency`

```python
from scipy.stats import chi2_contingency

pivot_table = pd.pivot_table(data=data, index='변수1', columns='변수2',
                            aggfunc='count') # 다른 변수가 DataFrame에 있다면 아무 값이나 value='변수3'으로 주어야함

# crosstab = pd.crosstab(index = data['변수1'], columns = data['변수2'])

chi2, p, dof, expected = chi2_contingency(pivot_table) # 또는 crosstab
```



## 머신러닝

| from                 | import                 | 용도                                        |
| -------------------- | ---------------------- | ------------------------------------------- |
| sklearn.tree         | DecisionTreeClassifier | 결정 나무(분류)                             |
| sklearn.tree         | plot_tree              | 이미지로 트리 확인<br />Root Node 확인 용도 |
| sklearn.tree         | export_text            | 텍스트로 트리 확인<br />Root Node 확인 용도 |
| sklearn.linear_model | LogisticRegression     | 로지스틱 분류                               |
| sklearn.metrics      | classification_report  | 분류 평가 지표 확인                         |

### tree

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

dt_clf = DecisionTreeClassifier()
dt_clf.fit(X, y)

# export_text(dt_clf, feature_names=list(X.columns))
plot_tree(dt_clf, feature_names=list(X.columns), class_names=y.unique())
```

