도서 : 파이썬 머신러닝 완벽 가이드

# Machine Learning

- 기계 학습
- 예측 / 의사결정

## Classification of Machine Learning

### Supervised?

- 지도(Supervised) 학습
  - Regression, Classification
- 비지도(Unsupervised) 학습
  - Clustering, 차원축소
- 준지도(Semi-supervised) 학습
- 강화(Reinforce) 학습
- 전이(Transfer) 학습

### Real time?

- 온라인 학습
  - 점진적으로 훈련
- 배치 학습
  - 모든 데이터를 사용해 학습, 오프라인

## Supervised Learning

- 지도 학습
- 입력값(Feature), 출력값(Label)이 함께 제시
- Output이 수치형이면 회귀, 범주형이면 분류
- 모델에 따른 알고리즘 종류
  - KNN(K-Nearest Neighbor, K-최근접이웃)
  - Linear Regression(선형 회귀 (수치형))
  - Logistic Regression(로지스틱 회귀 (범주형))
  - Support Vector Machine(서포트 벡터 머신)
  - Decision Tree(의사결정트리)
  - Random Forest(랜덤 포레스트)
  - 신경망

## Unsupervised Learning

- 비지도 학습
- 분류되지 않은 데이터의 특징만을 활용하여 결과 산출
- 적절한 군집을 찾거나 차원 축소를 하는데 이용
- 알고리즘
  - Clustering(군집분석)
    - K-Means(K-평균)
    - HCA(Hierarchical Cluster Analysis, 계층적 군집 분석)
    - DBSCAN
  - 시각화와 차원축소
    - PCA(Principal Component Analysis, 주성분 분석)
    - Kernel(커널) PCA
    - LLE(Locally-Linear Embedding, 지역적 선형 임베딩)
  - 이상치 탐지
    - 가우스 분포를 이용한 이상치 탐지
  - Association Rule(연관규칙)
    - Apriori
    - Eclat

## Semi-supervised Learning

- 준지도 학습
- 모든 데이터에 label을 달아줄 수 없는 현실적인 한계를 고려한 접근법
- 지도, 비지도 알고리즘 조합
- 알고리즘
  - DBN(심층신뢰신경만)
  - RBM(제한된 볼츠만 기계)

## Reinforce Learning

- 강화 학습
- Agent가 환경을 관찰하고 행동을 실행하고 그 결과 보상을 받음
- 보상을 얻기 위해 최상의 전략(policy)을 스스로 학습
- 알고리즘
  - SARSA
  - Q-Learning

