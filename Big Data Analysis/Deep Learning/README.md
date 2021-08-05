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

# DNN

- **D**eep **N**eural **N**etwork
- layer의 수가 2개 이상일 때

```python
mnist = models.Sequential()

# Hidden Layers
mnist.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
mnist.add(layers.Dense(256, activation='relu'))

# Output Layer : 10개의 categories 분류
mnist.add(layers.Dense(10, activation='softmax'))
```

## Overfitting Issue

1. 더 많은 Train Data

2. Model Capacity 낮추기

- 너무 많은 parameters가 문제
  - Input Size : 줄일 수 있으나 웬만하면 건들지 않기
  - Output Layer : 줄일 수 없음
  - Hidden Layer : 줄이면 Overfitting도 줄일 수 있으나 성능에 부정적인 영향

```python
mnist = models.Sequential()
mnist.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
mnist.add(layers.Dense(10, activation='softmax'))
```

- L2 Regularization
  - 마찬가지로 Overfitting은 줄일 수 있으나 성능에 부정적인 영향 (loss가 0이 되지 않음)

```python
from tensorflow.keras import regularizers

mnist = models.Sequential()
mnist.add(layers.Dense(512, activation='relu', input_shape=(28*28,),
                       kernel_regularizer=regularizers.l2(0.00001)))
mnist.add(layers.Dense(256, activation='relu',
                       kernel_regularizer=regularizers.l2(0.00001)))
mnist.add(layers.Dense(10, activation='softmax'))
```

- Dropout
  - 학습 과정에서 일부 연결을 무작위로 제외 시킴

```python
mnist = models.Sequential()
mnist.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
mnist.add(layers.Dropout(0.4)) # dropout할 연결의 비율
mnist.add(layers.Dense(256, activation='relu'))
mnist.add(layers.Dropout(0.2))
mnist.add(layers.Dense(10, activation='softmax'))
```

- Batch Normalization
  - 활성화 함수(ReLU 등)에 값을 넣기 전에 표준화 진행
  - Loss가 증가하지 않으면서 overfitting도 줄임
  - 구현할 때, activation 함수를 `Dense` 바깥으로 빼주는 것이 중요

```python
mnist = models.Sequential()
mnist.add(layers.Dense(512, input_shape=(28*28,)))
mnist.add(layers.BatchNormalization())
mnist.add(layers.Activation('relu'))
mnist.add(layers.Dense(256))
mnist.add(layers.BatchNormalization())
mnist.add(layers.Activation('relu'))
mnist.add(layers.Dense(10, activation='softmax'))
```

- [ipynb](05-02_DNN_mnist_Categorical_Classification_Overfitting_GPU.ipynb)


|                     | train_loss | validation_loss | eval_loss | eval_accuracy |
|---------------------|:----------:|:---------------:|:---------:|:-------------:|
| Original            | 2.0563e-09 |      0.4062     |  0.32649  |    0.98220    |
| Remove Layer        | 5.4985e-09 |      0.1934     |  0.15929  |    0.98260    |
| L2 Regularization   |   0.0102   |      0.1519     |  0.13205  |    0.97950    |
| Drop Out            |   0.0154   |      0.2392     |  0.21450  |    0.98200    |
| Batch Normalization | 8.9677e-04 |      0.1840     |  0.15993  |    0.98140    |
| L2 + Drop Out       |   0.0516   |      0.1050     |  0.09672  |    **0.98460**    |
| L2 + Batch          |   0.0168   |      0.1602     |  0.15973  |    0.98020    |
| Drop Out + Batch    |   0.0166   |      **0.0942**     |  **0.08306**  |    0.98140    |

- 할 때마다 결과는 달라질 수 있다.
- mnist 데이터에는 L2+Drop Out을 섞은 모델이 성능이 가장 좋았으나, 분석 데이터마다 바뀔 수 있다.

## Early Stopping

- 학습을 반복할수록 train data에 과적합되어, validation 또는 test data에 대한 성능이 낮아지는 것을 막기 위하여 학습을 빨리 끝내는 것

### EarlyStopping()

```python
from tensorflow.keras.callbacks import EarlyStopping

es = EarlyStopping(monitor='val_mae',
                   mode='min',
                   patience=50,
                   verbose=1)
```

- monitor : 모니터링 대상 성능
- mode : 모니터링 대상을 최대/최소화
  - mae, mse 등은 min, accuracy, recall, precision 등은 max
- patience : 성능이 개선되지 않는 epochs 횟수

### ModelCheckpoint()

```python
from tensorflow.keras.callbacks import ModelCheckpoint

mc = ModelCheckpoint('best_boston.h5',
                     monitor='val_mae',
                     mode='min',
                     save_best_only=True,
                     verbose=1)
```

- 'best_boston.h5' : 최적 모델이 저장될 경로
- save_best_only : 최적 모델만 저장할지 결정

