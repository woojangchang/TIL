'''분할정복 곱셈법
일반적인 행렬 곱셈법은 O(n**3)이라면
쉬트라쎈 곱셈법은 O(n**2.81)이므로 시간 복잡도가 적은 장점이 있다.'''


def strassen(A, B):
    n = len(A)

    if n <= threshold:
        return matrixmult(A,B)

    ''' n이 2의 거듭제곱수일 때만 가능한 쉬트라쎈 행렬 곱셈이므로
    나머지는 0으로 채워준다. '''
    k = 0
    while n > 2**k :
        k += 1
    m = 2 ** k
    newA = [[0] * m for _ in range(m)]
    newB = [[0] * m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            newA[i][j] = A[i][j]
            newB[i][j] = B[i][j]
    
    A11, A12, A21, A22 = devide(newA)
    B11, B12, B21, B22 = devide(newB)
    M1 = strassen(madd(A11, A22), madd(B11, B22))
    M2 = strassen(madd(A21, A22), B11)
    M3 = strassen(A11, msub(B12, B22))
    M4 = strassen(A22, msub(B21, B11))
    M5 = strassen(madd(A11, A12), B22)
    M6 = strassen(msub(A21, A11), madd(B11, B12))
    M7 = strassen(msub(A12, A22), madd(B21, B22))
    newC = conquer(M1, M2, M3, M4, M5, M6, M7)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = newC[i][j]
    return C

def devide(A):
    n = len(A)
    m = n // 2
    A11 = [[0] * m for _ in range(m)]
    A12 = [[0] * m for _ in range(m)]
    A21 = [[0] * m for _ in range(m)]
    A22 = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j+m]
            A21[i][j] = A[i+m][j]
            A22[i][j] = A[i+m][j+m]
    return A11, A12, A21, A22

def matrixmult(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def madd(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def msub(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def conquer(M1, M2, M3, M4, M5, M6, M7):
    C11 = madd(msub(madd(M1, M4), M5), M7)
    C12 = madd(M3, M5)
    C21 = madd(M2, M4)
    C22 = madd(msub(madd(M1, M3), M2), M6)
    m = len(C11)
    n = 2 * m
    C = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j+m] = C12[i][j]
            C[i+m][j] = C21[i][j]
            C[i+m][j+m] = C22[i][j]
    return C

import random
import time

n = 4
#A = [[random.randint(-5,5), random.randint(-5,5), random.randint(-5,5), random.randint(-5,5)] for _ in range(n)]
#B = [[random.randint(-5,5), random.randint(-5,5), random.randint(-5,5), random.randint(-5,5)] for _ in range(n)]
A = [
     [1,2,3,4],
     [5,6,7,8],
     [9,1,2,3],
     [4,5,6,7]
]

B = [
     [8,9,1,2],
     [3,4,5,6],
     [7,8,9,1],
     [2,3,4,5]
]

print('A')
for row in A :
    print(row)
print('B')
for row in B :
    print(row)

threshold = 2
print('strassen C')
x = time.time()
C = strassen(A,B)
print('{:.15f} seconds'.format(time.time()-x))
for row in C :
    print(row)

print('product C')
x = time.time()
C = matrixmult(A,B)
print('{:.15f} seconds'.format(time.time()-x))
for row in C :
    print(row)
