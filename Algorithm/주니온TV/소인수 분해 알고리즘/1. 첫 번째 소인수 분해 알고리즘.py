from time import time

def calculate_time(fn, n):
    now = time()
    factors = fn(n)
    print(f'{n} = {factors}')
    print(f'걸린 시간: {time()-now:.15f}초')


def addFactor(factors, i):
    if i in factors:
        factors[i] += 1
    else:
        factors[i] = 1

def factorize(n):
    assert isinstance(n, int) & (n > 0), "n must be natural number"

    factors = {}
    sqrtn = int(n**0.5)
    i = 2
    for i in range(2, sqrtn+1):
        while n % i == 0:
            addFactor(factors, i)
            n //= i
    
    if n > 1:
        addFactor(factors, n)
    
    return factors

calculate_time(factorize, 360)

def isprime(n):
    factors = factorize(n)
    return len(factors) == 1

for i in range(2, 33):
    n = (2 ** i) - 1
    if isprime(n):
        print(i, n, ":", factorize(n))


n = (2 ** 64) - 1
calculate_time(factorize, n)

# 18446744073709551615 = {3: 1, 5: 1, 17: 1, 257: 1, 641: 1, 65537: 1, 6700417: 1}
# 걸린 시간: 638.749000310897827초