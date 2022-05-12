# https://www.youtube.com/watch?v=z8KVLz9BFIo

################# 문제 정의 #################
X = ["A", "B", "C", "B", "D", "A", "B"] * 2
Y = ["B", "D", "C", "A", "B", "A"] * 2
# LCS(X, Y) = ["B", "C", "B", "A"], len(LCS) = 4


################# 함수 정의 #################
from time import time

def calculate_time(fn):
    now = time()
    S = fn(X, Y)
    print(f'len(LCS) = {S}')
    print(f'걸린 시간: {time()-now:.15f}초')


################# 알고리즘 #################
# 1) Brute-Force Approach
# exponential time complexity (2^m)
def lcs1(X, Y):
    lX = len(X)
    lY = len(Y)
    if lX == 0 or lY == 0:
        return 0
    elif X[-1]==Y[-1]:
        return lcs1(X[:-1], Y[:-1]) + 1
    else:
        return max(lcs1(X[:-1], Y), lcs1(X, Y[:-1]))

print('Brute-Force Approach')
calculate_time(lcs1)
print()


# 2) Dynamic Programming (memoization)
def lcs2(X, Y):
    X, Y = [' '] + X, [' '] + Y
    lX, lY = len(X), len(Y)
    c = [[0 for _ in range(lY)] for _ in range(lX)]
    for i in range(1, lX):
        for j in range(1, lY):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[-1][-1]

print('DP')
calculate_time(lcs2)
print()


# 최적해의 재구성
def lcs3(X, Y):
    X, Y = [' '] + X, [' '] + Y
    lX, lY = len(X), len(Y)
    c = [[0 for _ in range(lY)] for _ in range(lX)]
    b = [[0 for _ in range(lY)] for _ in range(lX)]
    for i in range(1, lX):
        for j in range(1, lY):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
                b[i][j] = 2 if (c[i][j-1] > c[i-1][j]) else 3
    return c[-1][-1], b

c, b = lcs3(X, Y)

def get_lcs(i, j, b, X):
    if i == 0 or j == 0:
        return ""
    else:
        if b[i][j] == 1:
            return get_lcs(i-1, j-1, b, X) + X[i]
        elif b[i][j] == 2:
            return get_lcs(i, j-1, b, X)
        elif b[i][j] == 3:
            return get_lcs(i-1, j, b, X)

print(get_lcs(len(X), len(Y), b, X))