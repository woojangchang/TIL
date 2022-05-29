from time import time

def calculate_time(fn, n):
    now = time()
    factors = fn(n)
    print(f'{n} = {factors}')
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


def addFactor(factors, i):
    if i in factors:
        factors[i] += 1
    else:
        factors[i] = 1

def factorize(n):
    assert isinstance(n, int) & (n > 0), "n must be natural number"

    factors = {}
    sqrtn = int(n**0.5)

    # sqrtn보다 작은 소수에 대해서만 for를 돌린다. (이전에는 sqrtn보다 작은 모든 수에 대해 시도)
    primes = findPrimes(sqrtn)
    for i in primes:
        while n % i == 0:
            addFactor(factors, i)
            n //= i
    
    if n > 1:
        addFactor(factors, n)
    
    return factors

calculate_time(factorize, 360) # 이전에는 0.001초, 바꾸면 0.000000000000... 초
# 그러나 n이 커질수록 O(루트n) = O(루트2^b) = O(2^b/2) (b=n의 비트 수) 지수적 시간 복잡도를 가짐