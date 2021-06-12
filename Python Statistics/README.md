※ csv 자료 : 누구나 파이썬 통계분석

# Chapter 2

## 데이터 지표

- 평균, 편차, 분산, 표준편차, 사분위범위

## 데이터 시각화

- 도수분포표, 계급값, 상대도수, 누적상대도수, 최빈값
- `matplotlib`을 이용한 히스토그램, 상대도수 히스토그램, 누적상대도수 꺾은선 그래프 그리기



# Chapter 3

## 관계 지표

- 공분산, 상관계수

## 시각화

- 산점도, 회귀직선, 히트맵

## 앤스컴의 예

- 시각화의 중요성



# Chapter 4

## 모집단과 표본

- 모집단, 표본, 복원추출, 비복원추출

## 확률 모형

- 확률 분포



# Chapter 5

## 1차원 이산형 확률변수

- 기댓값, 분산

## 2차원 이산형 확률변수

- 결합확률분포, 주변확률분포
- 기댓값, 분산, 공분산, 상관계수



# Chapter 6

## 베르누이 분포

$$
f(x) = \begin{cases}p^x(1-p)^{(1-x)} & (x\in\{0,1\}) \\ 0 & (otherwise) \end{cases} \\
X\sim Bern(p) 일\ 때 \ E(X) =p, \ V(X)=p(1-p)
$$

## 이항분포

$$
f(x) = \begin{cases}_nC_xp^x(1-p)^{(n-x)} & (x\in\{0,1,...,n\}) \\ 0 & (otherwise) \end{cases} \\
X\sim Bin(n,p) 일\ 때 \ E(X)=np, \ V(X) = np(1-p)
$$

## 기하분포

$$
f(x) = \begin{cases} (1-p)^{(x-1)}p & (x\in \{1,2,3,...\}) \\ 0 & (otherwise) \end{cases} \\
X\sim Ge(p)일\ 때 \ E(X) = {{1} \over {p}}, V(X) = {{(1-p)} \over {p^2}}
$$

## 포아송 분포

$$
f(x) = \begin{cases}{ {\lambda ^x} \over {x!} } e^{-\lambda } & (x\in \{0, 1, 2, ...\}) \\ 0 & (otherwise) \end{cases} \\
X \sim Poi(\lambda) 일\ 때 \ E(X)=\lambda, \ V(X) = \lambda
$$

