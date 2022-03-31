import time

def fib(n):
    if n < 2 :
        return n
    else :
        return fib(n-1) + fib(n-2)


def fib2(n):
    f = [0] * (n+1)
    if n>0 :
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1]+f[i-2]
    return f[n]

def fib3(n):
    if n < 2 :
        return n
    else :
        x = 0
        y = 1
        for i in range(2, n+1):
            f = x + y
            x = y
            y = f
        return f
time1 = time.time()
print(fib(30))
print(time.time()-time1)

time2 = time.time()
print(fib2(100))
print(time.time()-time2)

time3 = time.time()
print(fib3(100))
print(time.time()-time3)
