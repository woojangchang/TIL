def ladd(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    result = []
    carry = 0
    for k in range(n):
        i = u[k] if (k < len(u)) else 0
        j = v[k] if (k < len(v)) else 0
        value = i + j + carry
        carry = value // 10
        result.append(value%10)

    if carry > 0 :
        result.append(carry)
    return result

def lsub(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    result = []
    borrow = 0
    for k in range(n):
        i = u[k] if (k < len(u)) else 0
        j = v[k] if (k < len(v)) else 0

        value = i - j + borrow
        if value < 0 :
            value += 10
            borrow = -1
        else :
            borrow = 0
        result.append(value%10)
    if borrow < 0 :
        print("음의 정수는 처리 못함.")
    return result

# 단순 계산 : O(n**2)
# Devide And Conquer1 : Worst O(n**2)
def prod(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    if len(u) == 0 or len(v) == 0 :
        return [0]
    elif n <= thresold :
        return lmult(u, v)
    else :
        m = n // 2
        x = div(u,m)
        y = rem(u, m)
        w = div(v, m)
        z = rem(v, m)
        p1 = prod(x, w)
        p2 = ladd(prod(x, z), prod(y, w))
        p3 = prod(y, z)
        return ladd(ladd(exp(p1, 2*m), exp(p2, m)), p3)

# O(n**1.58), 재귀호출 3번
def prod2(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    if len(u) == 0 or len(v) == 0 :
        print(u, v, [0])
        return [0]
    elif n <= thresold :
        print(u, v, lmult(u, v)[::-1])
        return lmult(u, v)
    else :
        m = n // 2
        x = div(u,m)
        y = rem(u, m)
        w = div(v, m)
        z = rem(v, m)
        r = prod2(ladd(x, y), ladd(w, z))
        p1 = prod2(x, w)
        p3 = prod2(y, z)
        p2 = lsub(r, ladd(p1, p3))
        print(ladd(ladd(exp(p1, 2*m), exp(p2, m)), p3))
        return ladd(ladd(exp(p1, 2*m), exp(p2, m)), p3)

def exp(u, m):
    if u == [0] :
        return [0]
    else :
        return ([0]*m)+u
        
def div(u, m):
    if len(u) < m :
        u.append(0)
    return u[m:]

def rem(u, m):
    if len(u) < m :
        u.append(0)
    return u[:m]

def lmult(u, v):
    i = u[0] if 0 < len(u) else 0
    j = v[0] if 0 < len(v) else 0
    value = i * j
    carry = value // 10
    result = []
    result.append(value % 10)
    if carry > 0:
        result.append(carry)
    return result

# u = 9124, v = 11087
u = [4, 2, 1, 9]
v = [7, 8, 0, 1, 1]

w = ladd(u, v)
print(w[::-1])
print(9124+11087)

thresold = 1
y = prod(u, v)
print(y[::-1])
print(9124*11087)

#z = prod2([8,1], [2,0,5])
#print(z[::-1])
#print(18*502)
