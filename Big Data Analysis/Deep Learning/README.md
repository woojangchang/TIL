- google colab 환경으로 진행

# Artificial Neural Network

- 인공 신경망
- Perceptron

$$
y = XW+b && \\
= \left[
\begin{matrix}
    x_{11} & ... & x_{1n} \\
    ... & ... & ... \\
    x_{m1} & ... & x_{mn}
\end{matrix}
\right] \left[
\begin{matrix}
    w_{11} & ... & w_{1t} \\
    ... & ... & ... \\
    w_{n1} & ... & w_{nt}
\end{matrix}
\right]+ \left[
\begin{matrix}
    b_1 \\ ... \\ b_t
\end{matrix}
\right]
$$

- 데이터의 개수 : m, feature 개수 : n, output 개수 : t

- Multi Layer Perceptron
  - 여러 Layer의 Perceptron(함수)으로 이루어진 신경망
  - Fully Connected : 모두가 이어져 있는 신경망
  - 경사하강법을 사용하여 W, b 학습
  - [ipynb](01-01_Multi_Layer_Perceptron_XOR_CPU.ipynb)
- Softmax
  - 전체 출력값의 합=1 > 학습 효과 증가 (다중 분류 수행)
  - [ipynb](01-04_Softmax_Activation_CPU.ipynb)

$$
f(x_k)=\dfrac{\exp(x_k-m)}{\sum_{i=1}^n\exp(x_i-m)}, m=\max(x_k)
$$

# Error Backpropagation

- 각 학습 단계의 parameter (W, b)를 update하기 위하여 마다의 편미분값 필요
  - 데이터 수가 많을 수록, 노드가 많을 수록, layer가 깊어질수록 그 수는 늘어나기 때문에 연산 시간이 오래 걸림 [(ipynb)](01-02_MLP_Gradient_Descent_CPU.ipynb)

## Backpropatation

- 편미분값 계산 없이 경사값 계산

$$
\dfrac{\part \text{Cost}}{\part W}=\dfrac{\part \text{Cost}}{\part \hat y} \dfrac{\part \hat y}{\part WS} \dfrac{\part WS}{\part W} \\=\text{오차값}\cdot\text{출력값}(1-\text{출력값})\cdot\text{입력값}
$$

- WS : Weight Sum, y : output
- [ipynb](02-02_Error_Backpropagation_CPU.ipynb)

## Vanishing Gradient

- 시그모이드 함수를 미분하면 최대치가 0.25
- 은닉층이 증가하면 그 값이 계속 곱해져 기울기가 0이 되는 문제 발생
- 대응책 : 다른 함수 사용
  - Tanh, ReLU, Leaky ReLU

# Optimization Method

- 기존 Gradient Descent의 단점을 보완하는 방법
  - Local Minimum에서 빠져나오지 못하고 Global Minimum을 찾지 못하는 문제 등
- 수식은 외우지 못하더라도 이런 방법들이 있다는 것은 꼭 기억해둘 것

## Stochastic Gradient Descent(SGD)

- 전체 데이터 대신 일부 데이터 사용
- 전체를 이용한 것보다 부정확할 수 있으나 계산 속도가 훨씬 빠름

$$
W_{t+1}=W_t - \gamma \cdot \dfrac{\part J}{\part \theta}
$$

## Momentum

- 이동 과정에 관성을 반영
- 바로 직전 시점의 가중치 업데이트 변화량을 적용

$$
dW_{t+1} = W_t - W_{t-1} \\
W_{t+1} = W_t - \gamma \cdot \dfrac{\part J}{\part \theta} + \mu \cdot dW_{t-1}
$$

## Adaptive Gradient (Adagrad)

- 학습 횟수가 증가함에 따라 학습률을 조절하는 옵션 추가

## RMSProp

- Root Mean Square Propagation
- Adagrad의 단점인 Gradient 제곱합을 지수평균으로 대체

## Adam

- Adaptive Moment Estimation
- RMSProp과 Momentum 방식의 장점을 합친 알고리즘

# Tensorflow

```python
from tensorflow.keras import models, layers

Model_iris = models.Sequential()

# 첫 번째 hidden layer의 개수=16, input의 shape 명시
Model_iris.add(layers.Dense(16, activation='relu', input_shape=(4,))) 
# 두 번째 hidden layer의 개수=8
Model_iris.add(layers.Dense(8, activation='relu')) 
# output layer의 개수=3=output의 shape, 다중분류이므로 softmax
Model_iris.add(layers.Dense(3, activation='softmax')) 
```

```python
Model_iris.compile(loss='categorical_crossentropy',
                   optimizer='adam',
                   metrics=['accuracy'])
```

```python
History_iris = Model_iris.fit(X_train, y_train,
                              epochs=500, # propagation 반복 횟수 (학습 횟수)
                              batch_size=7, # 105개의 train data를 7개씩 나누어서 15번 반복
                              validation_data=(X_test, y_test))
```

