import random
import pandas as pd
import numpy as np
import time


class EarlyStopping:
    def __init__(self, patience=5):
        self.loss = np.inf
        self.patience = 0
        self.patience_limit = patience
        
    def step(self, loss):
        if self.loss > loss:
            self.loss = loss
            self.patience = 0
        else:
            self.patience += 1
    
    def is_stop(self):
        return self.patience >= self.patience_limit


def generate_feature(condition:dict, base:pd.Series, fix_features:dict) -> pd.Series:
    """
    첫 세대의 각 데이터 생성
    
    Parameters
    ----------
    condition: 해의 범위
        {'F1':{'mean':0, 'std':3, 'min':-100, 'max':100}, 'F2':{'mean':10, 'std':3, 'min':-100, 'max':50}}
        * 필요시 condition2 = dataset.dtypes를 넣을 것 (해의 데이터 타입을 위함 int/float)
            if condition2[col] == 'float64':
                x = x
            else:
                x = int(x)
    base: 생성 기준 (pd.Series)
    fix_features: 고정시킬 features
        {'F1':100, 'F2':50, ...}
    
    Returns
    -------
    pd.Series
    
    
    Examples
    --------
    condition = dataset.describe().to_dict()
    base = dataset.iloc[-1]
    fix_features = base[some_features].to_dict()
    
    new_feature = generate_feature(condition, base, fix_features)
    
    """
    
    indivisual = base.copy()
    for col, value in condition.items():
        if col in fix_features.keys():
            indivisual[col] = fix_features[col]
            continue
        
        maximum = value['max']
        minimum = value['min']
        
        x = random.uniform(minimum, maximum)
    
        indivisual[col] = np.round(x, 3)
    
    return indivisual


def generate_population(size:int, condition:dict, base:pd.Series, fix_features:dict) -> list:
    """
    첫 세대 생성.
    
    Parameters
    ----------
    size: 생성할 데이터의 개수
    condition: 해의 범위
        {'F1':{'mean':0, 'min':-100, 'max':100}, 'F2':{'mean':10, 'min':-100, 'max':50}}
    base: 생성 기준 (pd.Series)
    fix_features: 고정시킬 features
        {'F1':100, 'F2':50, }
    
    
    Returns
    -------
    list [pd.Series, pd.Series, ...]
    
    
    Examples
    --------
    size = 100
    condition = dataset.describe().to_dict()
    base = dataset.iloc[-1]
    fix_features = base[some_features].to_dict()
    
    population = generate_population(size, condition, base, fix_features)
    
    """
    population = []
    
    for i in range(size):
        indivisual = generate_feature(condition, base, fix_features)
        population.append(indivisual)
        
    return population



def compute_performance(fitness, population:list) -> list:
    """
    세대의 모든 데이터에 대해 loss 계산하여 오름차순 정렬
    
    Parameters
    ----------
    fitness: loss 계산식.
        - input: indivisual(pd.Series)
        - return: loss (float)
    population: 세대 데이터 리스트
    
    
    
    Returns
    -------
    list [(pd.Series, loss), (pd.Series, loss), ...]
    
    
    Examples
    --------    
    population = [test.iloc[0], test.iloc[1], test.iloc[2]]
    population_sorted = compute_performance(fitness, population)
    # [(test.iloc[2], 10), (test.iloc[0], 50), (test.iloc[1], 80)]
    
    """
    performance_list = []
    for indivisual in population:
        loss = fitness(indivisual)
        
        performance_list.append([indivisual, loss])
    
    population_sorted = sorted(performance_list, key=lambda x:x[1], reverse=False)
    return population_sorted


def select_survivors(population_sorted:list, best_sample:int, lucky_few:int) -> list:
    """
    한 세대에서 살릴 데이터를 선택 (부모 데이터 선택)
    
    Parameters
    ----------
    population_sorted: loss가 낮은 순으로 정리된 세대 데이터
    best_sample: loss가 낮은 `best_sample` 수만큼 다음 세대로 넘김
    lucky_few: best_sample을 제외한 나머지 데이터 중 랜덤으로 `lucky_few` 만큼 다음 세대로 넘김
    
    
    Returns
    -------
    list [pd.Series, pd.Series, ...]
    
    
    Examples
    --------
    population_sorted = compute_performance(fitness, population)
    # len(population) == 100
    best_sample = 10
    lucky_few = 10
    
    parents = select_survivors(population_sorted, best_sample, lucky_few)
    # len(parents) == 20
    
    """
    
    # best_sample 수만큼 다음 세대로 보냄
    parents = [population_sorted[i][0] for i in range(best_sample)]
    
    
    # 랜덤으로 운이 좋은 부모들을 살림
    lucky_survivors = random.sample(population_sorted[best_sample:], k=lucky_few)
    for I in lucky_survivors:
        parents.append(I[0])
        
    # 다음 세대의 부모들을 섞음
    random.shuffle(parents)
    
    return parents


def create_child(indivisual1:pd.Series, indivisual2:pd.Series) -> pd.Series:
    """
    두 유전자를 교배하여 새로운 유전자 생성
    
    Parameters
    ----------
    indivisual1, indivisual2: 값을 섞을 두 데이터
    
    
    Returns
    -------
    pd.Series
    
    
    Examples
    --------
    indivisual1 = next_generation[0]
    indivisual2 = next_generation[-1]
    child = create_child(indivisual1, indivisual2)
    
    """
    child = []
    for i in range(len(indivisual1)):
        if random.random() < 0.5: # 50% 확률로 1의 유전자 획득
            child.append(indivisual1[i])
        else: # 50% 확률로 2의 유전자 획득
            child.append(indivisual2[i])
    return pd.Series(child, index=indivisual1.index)

# 정규분포에 따라 노이즈 추가
def mutate_feature(indivisual:pd.Series, condition:dict, fix_features:dict) -> pd.Series:
    """
    정규분포 확률에 따라 노이즈 추가
    
    Parameters
    ----------
    indivisual: 노이즈를 추가할 원본 데이터
    condition: 해의 범위
        {'F1':{'mean':0, 'min':-100, 'max':100}, 'F2':{'mean':10, 'min':-100, 'max':50}}
    fix_features: 고정시킬 features
        {'F1':100, 'F2':50, }
        
    
    Returns
    -------
    pd.Series
    
    
    Examples
    --------
    indivisual1 = next_generation[0]
    indivisual2 = next_generation[-1]
    child = create_child(indivisual1, indivisual2)
    
    condition = dataset.describe().to_dict()
    fix_features = base[some_features].to_dict()
    
    mutated = mutate_feature(child, condition, fix_features)
    """
    indivisual = indivisual.copy()
    for i, (col, value) in enumerate(condition.items()):
        if col in fix_features.keys():
            indivisual[col] = fix_features[col]
            continue
            
        maximum = value['max']
        minimum = value['min']
        
        x = random.uniform(minimum, maximum)
        
        indivisual[col] = np.round(x, 3)
        
    return indivisual


def create_children(parents:list, n_child:int, chance_of_mutation:int, condition:dict, fix_features:dict) -> list:
    """
    교배, 변이 등을 통해 다음 세대 생성
    
    Parameters
    ----------
    parents: 한 세대에서 선택된 부모 데이터
    n_child: 부모 한 쌍으로 만들어낼 자식 수
    chance_of_mutation: 돌연변이를 만들 확률(%)
    condition: 해의 범위
        {'F1':{'mean':0, 'min':-100, 'max':100}, 'F2':{'mean':10, 'min':-100, 'max':50}}
    fix_features: 고정시킬 features
        {'F1':100, 'F2':50, }
    
    
    Returns
    -------
    list [pd.Series, pd.Series, ...]
    
    
    Examples
    --------
    parents = select_survivors(population_sorted, best_sample, lucky_few) # len(parents) == 20
    n_child = 10
    chance_of_muation = 10
    
    condition = dataset.describe().to_dict()
    fix_features = base[some_features].to_dict()
    
    next_generation = create_children(parents, n_child, chance_of_mutation, condition, fix_features)
    # len(next_generation) == 100 <=> (len(parents)// 2) * n_child == 100
    
    """
    # chance_of_mutaion 만큼 돌연변이 생성
    next_population = []
    for i in range(len(parents)//2):
        for j in range(n_child):
            child = create_child(parents[i], parents[-i-1])
            if random.random() * 100 < chance_of_mutation:
                child = mutate_feature(child, condition, fix_features)
            next_population.append(child)
    return next_population






class GeneticAlgorithm:

    def search(self, condition, fitness, n_generation, population, best_sample,
               lucky_few, n_child, chance_of_mutation, fix_features, tolerance, base,
               es=None, verbose=True, time_limit=None):
        """
        condition: 해의 범위
        fitness: loss 계산식
            - input: indivisual(pd.Series)
            - return: loss (float)
        n_generation: 반복할 세대 수, int
        population: 세대 당 인구 수, int
        best_sample: 세대에서 살릴 best 샘플 수
        lucky_few: 운 좋게 살릴 샘플 수
        n_child: 자식 수
        chance_of_mutation: 돌연변이 확률, int(%)
        fix_features: feature 중 고정할 값, dict
        tolerance: 알고리즘 종료 점수
        base: 최초 설정 값
        es: EarlyStopping (int 또는 EarlyStopping class)
        verbose: log 출력 여부
            - True인 경우 출력, False면 출력하지 않음
        time_limit: 탐색 시간 제한. 기본값 None
            - n_generation, es보다 우선
        """
        assert ((best_sample + lucky_few) // 2) * n_child == population, "((best_sample + lucky_few) // 2) * n_child == population"
        
        # EarlyStopping 설정
        if isinstance(es, int):
            es = EarlyStopping(patience=es)
            
        elif es is None:
            es = EarlyStopping(patience=n_generation)
        
        # 학습 과정 저장
        self.best = base
        self.loss = np.inf
        start = time.time()
        
        time_total = 0
        
        # 최초 세대 생성
        pop = generate_population(size=population, condition=condition, base=base, fix_features=fix_features)
        for g in range(n_generation):
            # 세대의 loss 계산
            pop_sorted = compute_performance(fitness, population=pop)
            
            # 가장 loss가 낮은 데이터 확인
            es.step(pop_sorted[0][1])
            if es.is_stop(): # EarlyStopping 횟수만큼 loss 개선이 없으면 stop
                end = time.time()
                elapsed_time = end - start
                print(f"Early Stopped at generation {g+1}/{n_generation}")
                print(f'Elapsed Time: {elapsed_time:.2f}s, Loss: {self.loss}')
                break

            if pop_sorted[0][1] < self.loss: # 이전 loss보다 좋아지면 저장
                self.best = pop_sorted[0][0]
                self.loss = pop_sorted[0][1]

            if self.loss <= tolerance: # 차이가 허용범위 이하면 완료
                end = time.time()
                elapsed_time = end - start
                print(f"SUCESSED at generation {g+1}/{n_generation}")
                print(f'Elapsed Time: {elapsed_time:.2f}s, Loss: {self.loss}')
                break

            # 부모 선택
            survivors = select_survivors(population_sorted=pop_sorted, best_sample=best_sample, lucky_few=lucky_few)

            # 부모를 이용한 다음 세대 생성
            new_generation = create_children(parents=survivors, n_child=n_child, 
                                             chance_of_mutation=chance_of_mutation, condition=condition,
                                             fix_features=fix_features)

            pop = new_generation

            end = time.time()
            elapsed_time = end - start
            
            time_total += elapsed_time
            # 시간 제한 초과 시 종료
            if time_limit is not None:
                if time_total > time_limit:
                    print(f"Time limit exceeded at generation {g+1}/{n_generation}")
                    print(f'Total Time: {time_total:.2f}s, Loss: {self.loss}')
                    break

            
            if verbose:
                print(f'Generation {g+1}/{n_generation}')
                print(f'Elapsed Time: {elapsed_time:.2f}s, Loss: {self.loss}')

            start = time.time()
        
        return self.best