# Sum of N to M
from time import time

N, M = map(int, input().split())
def calculate_time(fn):
    now = time()
    S = fn(N, M)
    print(f'Sum of {N} to {M} = {S}')
    print(f'걸린 시간: {time()-now:.15f}초')


# 0. python range
def sum0(N, M):
    S = sum(range(N, M+1))
    return S

print('Python Range')
calculate_time(sum0)
print()

# 1. recursion
def sum1(N, M):
    if N == M:
        return N
    else:
        return N + sum1(N+1, M) # sum1(N, M-1) + M

print('Recursion')
calculate_time(sum1)
print()

# 2. tail recursion
def sum2(N, M, S):
    if N == M:
        return S + N
    else:
        return sum2(N+1, M, S+N)

def calculate_time2(fn):
    now = time()
    S = fn(N, M, 0)
    print(f'Sum of {N} to {M} = {S}')
    print(f'걸린 시간: {time()-now:.15f}초')

print('Tail Recursion')
calculate_time2(sum2)
print()

# 3. devide & conquer
def sum3(N, M):
    if N == M:
        return N
    else:
        mid = (N + M) // 2
        return sum3(N, mid) + sum3(mid+1, M)

print('Devide & Conquer')
calculate_time(sum3)
print()

# 4. dynamic programming
def sum4(N, M):
    S = 0
    for i in range(M, N-1, -1):
        S += i
    return S

print('Dynamic Programmig')
calculate_time(sum4)
print()

# 5. mathematically
def sum5(N, M):
    S = (M * (M + 1) - N * (N - 1)) // 2
    return S

print('Mathematically')
calculate_time(sum5)
print()