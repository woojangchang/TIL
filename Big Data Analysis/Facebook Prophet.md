# Facebook Prophet

시계열 분석을 기존의 ARIMA 등의 방법보다 쉽게 할 수 있도록 도와주는 파이썬 라이브러리 + 미래 예측

## Installation

1. Anaconda Prompt 실행
2. `conda deactivate`
3. `conda create --name prophet python=3.8.3`
4. `conda activate prophet`
5. `pip install ipykernel`
6. `python -m ipykernel install --user --name prophet --display-name "Python prophet"`
7. `conda install -c conda-forge fbprophet`
8. python 콘솔에서 `import fbprophet` 했을 때 No Module 오류가 뜨지 않는다면 설치 완료
   - `Importing plotly failed. Interactive plots will not work.` 경고문은 우선 무시
   - `pip install plotly` (또는 `pip install --upgrade plotly`)을 하면 해결
9.  jupyter lab 환경에서 작동이 되지 않으면 `conda install -c conda-forge jupyterlab`으로 해결

## Run

### Fit

```python
from fbprophet import Prophet

m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df) # df는 pandas로 불러온 데이터 프레임
```

- 다양한 옵션이 있으니 매뉴얼 참고

### Predict

```python
future = m.make_future_dataframe(30, freq='D')  # 30일
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
```

```python
fig1 = m.plot(forecast)
```

```python
fig2 = m.plot_components(forecast)
```



### Holiday

https://facebook.github.io/prophet/docs/seasonality,_holiday_effects,_and_regressors.html

```python
m = Prophet(holidays=holidays)
forecast = m.fit(df).predict(future)
```

- `holidays`는 위 github 참고해서 지정

```python
# Republic of Korea
m.add_country_holidays(country_name='KR')
```

