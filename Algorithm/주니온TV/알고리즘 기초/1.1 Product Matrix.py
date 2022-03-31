import random

def productMatrix(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

    return C

n = 2
A = [[random.randint(-5,5), random.randint(-5,5)] for _ in range(n)]
B = [[random.randint(-5,5), random.randint(-5,5)] for _ in range(n)]
for row in A :
    print(row)

for row in B :
    print(row)

C = productMatrix(A,B)
for row in C :
    print(row)

n = 3
A = [[random.randint(-5,5), random.randint(-5,5), random.randint(-5,5)] for _ in range(n)]
B = [[random.randint(-5,5), random.randint(-5,5), random.randint(-5,5)] for _ in range(n)]
for row in A :
    print(row)

for row in B :
    print(row)
C = productMatrix(A,B)
for row in C :
    print(row)
