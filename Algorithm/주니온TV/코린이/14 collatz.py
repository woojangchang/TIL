def collatz(n):
    seq = [n]
    while n>1 :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = 3*n + 1
        seq.append(n)
    return seq

def lenseq(l):
    i = 1
    while True :
        if len(collatz(i)) == l :
            return i
            break
        else :
            i += 1

def leastcollatz(n):
    l = 0
    m = 1
    for i in range(1,n+1):
        if l < len(collatz(i)) :
            l = len(collatz(i))
            m = i
    return m, l

n = 0
i = 0
while n < 10 :
    i += 1
    if len(collatz(i)) > 500 :
        n += 1
        l = len(collatz(i))
print(i, l)
