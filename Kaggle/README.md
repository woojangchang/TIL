# Data Leakage

https://www.kaggle.com/alexisbcook/data-leakage

**데이터 누수**란 **훈련 데이터의 정보를 실제 예측에서 사용할 수 없는 경우** 발생하며 타겟 누수(target leakage)와 훈련-테스트 오염(train-test contamination)이 있다.

## Target Leakage

예측 시점에서 사용할 수 없는 데이터가 데이터 셋에 포함되어 있을 때 발생

| got_pneumonia | age  | weight | male  | took_antibiotic_medicine | ...  |
| :-----------: | :--: | :----: | :---: | :----------------------: | :--- |
|     False     |  65  |  100   | False |          False           | ...  |
|     False     |  72  |  130   | True  |          False           | ...  |
|     True      |  58  |  100   | False |           True           | ...  |

폐렴에 걸렸는지(`got_pneumonia`)를 확인하기 위하여 항생제를 복용하는지(`took_antibiotic_medicine`)를 변수로 사용하는 경우 타겟 누수가 발생했다고 할 수 있다.

왜냐하면 시간 순서 혹은 원인과 결과가 반대이기 때문. 즉 항생제를 복용한 후 폐렴(복용했기 때문에 폐렴)이 아닌, 폐렴이 걸렸기 때문에 항생제를 복용한다고 봐야하기 때문이다.

그러므로 타겟 누수를 방지하려면 타겟 값이 결정된(생성된) 이후 파생된 변수를 제거해야한다.

## Train-Test Contamination

훈련-테스트 데이터로 쪼개기 전 scaling을 하는 경우 등에서 발생

실제 예측을 위한 데이터에 대한 기초 통계 정보(평균, 분산 등)이 없음에도 train_test_split을 하기 전 scaling을 한다는 것 자체가 잘못된 것. 즉, train_test_split 이후 test 데이터는 정말 처음 보는 값으로 생각하고 scaling을 train 데이터에만 적용한 뒤(fit_transform) 이후 test 데이터에 적용(transform)하여야 한다는 것.

같은 논리로, 교차검증을 할 때에도 전체 데이터에 대해 scaling을 하는 것이 아닌, train-validation으로 쪼갠 이후 train 데이터에 fit_transform, validation 데이터에 transform하여야 한다.

이에 대하여 잘 설명해놓은 블로그 : https://blog.naver.com/tjdudwo93/221085844907

![img](https://postfiles.pstatic.net/MjAxNzA4MzBfMjAz/MDAxNTA0MDk1MDE4NDU2.3Gx0IVIcMk9rlkxQv0bqlOFLUM30Dv5i0lsEimrBPygg.qExWYpz8_3UxQtEZytqAUbo0RELqmySAulqnCYclAzog.PNG.tjdudwo93/2.PNG?type=w3)

# Scatter Plots

## scatterplot

산점도를 확인할 때 사용

```python
sns.scatterplot(data=candy_data, x='sugarpercent', y='winpercent')
```

![image-20211026164755679](README.assets/image-20211026164755679.png)



카테고리별로 색을 다르게 하고 싶을 땐 `hue` 파라미터 이용

```python
sns.scatterplot(data=candy_data, x='pricepercent', y='winpercent', hue='chocolate')
```

![image-20211026164907449](README.assets/image-20211026164907449.png)

## regplot

산점도에 회귀직선까지 함께 나타내고 싶을 때 사용

```python
sns.regplot(data=candy_data, x='sugarpercent', y='winpercent')
```

![image-20211026164828986](README.assets/image-20211026164828986.png)

## lmplot

산점도에 회귀직선을 카테고리별로 따로 나타내고 싶을 때 사용

```python
sns.lmplot(data=candy_data, x='pricepercent', y='winpercent', hue='chocolate')
```

![image-20211026165020858](README.assets/image-20211026165020858.png)

## swarmplot

카테고리 변수마다 수치형 변수가 어떻게 모여있는지 (분포를) 확인하려고 할 때 사용

```python
sns.swarmplot(data=candy_data, x='chocolate', y='winpercent')
```

![image-20211026165154842](README.assets/image-20211026165154842.png)

# Distributions

## distplot

값의 분포를 알아보기 위할 때 사용

```python
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)
```

![image-20211026170823267](README.assets/image-20211026170823267.png)

## kdeplot

**kernel density estimate (KDE)**, 값의 분포를 부드러운 곡선으로 나타내기 위할 때 사용

```python
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
```

- `shade=True` : 곡선 아래 면적을 색칠

![image-20211026170830498](README.assets/image-20211026170830498.png)

## jointplot

2개의 분포를 겹쳐 등고선을 그리고자 할 때 사용

```python
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
```

![image-20211026170913858](README.assets/image-20211026170913858.png)

# Custom Styles

```python
sns.set_style("dark")
```

- (1) `"darkgrid"`, (2) `"whitegrid"`, (3) `"dark"`, (4) `"white"`, (5) `"ticks"` 등이 있음

