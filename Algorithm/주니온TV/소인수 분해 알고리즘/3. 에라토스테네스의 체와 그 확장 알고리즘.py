from time import time

def calculate_time(fn, n):
    now = time()
    primes = fn(n)
    print(f'{n}보다 작은 소수의 갯수: {len(primes)}')
    print(f'걸린 시간: {time()-now:.15f}초')


def isPrime(n):
    sqrtn = int(n**0.5)
    for i in range(2, sqrtn+1):
        if n%i == 0:
            return False
    return True

def findPrimes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes

# calculate_time(findPrimes, 2**21-1) # 11.5초


# 에라토스테네스의 체
def sieve(n):
    flags = [0, 0] + [1] * (n-1)
    sqrtn = int(n**0.5)
    # 체 정리
    for i in range(2, sqrtn+1):
        if flags[i] ==1:
            for j in range(i*i, n+1, i): # 2i, 3i, ... 등은 이미 2의 배수, 3의 배수, ...로 걸러졌기 때문에 i*i부터 시작하면 된다.
                flags[j] = 0
    
    # 소수 수집
    primes = []
    for i in range(len(flags)):
        if flags[i] == 1:
            primes.append(i)

    return primes



calculate_time(sieve, 2**21-1) # 0.4초


# n이 엄청 큰 수인 경우(메모리 부족 현상)
# 세그먼트 에라토스테네스의 체
# n을 sqrt(n)개의 세그먼트로 분할
# 첫 번째 세그먼트에서 소수를 모두 찾은 뒤 다음 세그먼트들을 차례로 방문하여 처리