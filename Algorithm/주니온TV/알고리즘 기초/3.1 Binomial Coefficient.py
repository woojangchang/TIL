import time

# Devide and Conquer 방식으로 이항계수 구하기 (비효율적)
def bin0(n, k):
    if k == 0 or n == k :
        return 1
    else :
        return bin0(n-1,k-1)+bin0(n-1,k)

# 내가 짠 동적계획 이항계수 구하기
def bin1(n, k):
    result = [[1]]
    for i in range(1, n+1):
        tmp = []
        for j in range(min(i,k+1)):
            if j == 0 :
                tmp.append(1)
            else :
                tmp.append(result[i-1][j-1]+result[i-1][j])
        tmp.append(1)
        result.append(tmp)
    return result[n][k]

# 동적계획으로 이항계수 구하기
def bin2(n, k):
    B = [[0] * (k+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j == 0 or j == i :
                B[i][j] = 1
            else :
                B[i][j] = B[i-1][j-1]+B[i-1][j]
    return B[n][k]

# 효율적인 이항계수 계산 nCk = nCn-k 임을 이용, 2차원 배열을 1차원으로
def bin3(n,k):
    if k > n // 2 :
        k = n-k
    B = [0] * (k+1)
    B[0] = 1
    for i in range(1, n+1):
        j = min(i, k)
        while j > 0 :
            B[j] = B[j] + B[j-1]
            j -= 1
    return B[k]

# print(bin0(30,15)) # 58.956초


x=time.time()
print(bin1(30,20)) # 0.025초
print(time.time()-x)

time.sleep(1)

x=time.time()
print(bin2(30,20)) # 0.007초
print(time.time()-x)

time.sleep(1)

x=time.time()
print(bin3(30,20))
print(time.time()-x)
