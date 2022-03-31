from time import time

u, v = map(int, input('큰 두 정수 입력: ').split())
print()
threshold = 1

def calculate_time(fn):
    now = time()
    uv = fn(u, v)
    print(f'{u}×{v}={uv}')
    print(f'걸린 시간: {time()-now:.8f}초')

# 일반적인 계산
print('Python 내장 곱셈 알고리즘')
calculate_time(lambda u, v:u*v)
print()


# Devide & Conquer > 시간 복잡도: O(n**2) (=4*T(n/2)+cn = O(n**log_2^4))
# u = x * 10**m + y, v = w * 10**m + z
# uv = xv*10**2m + (xz+yw)*10**m + yz
def large_mult(u, v):
    global threshold

    n = max(len(str(u)), len(str(v)))
    if u == 0 or v == 0:
        return 0
    elif n == threshold:
        return u * v
    else:
        m = n // 2
        x, y = u // 10**m, u % 10**m
        w, z = v // 10**m, v % 10**m
        p1, p2 = large_mult(x, w), large_mult(x, z)
        p3, p4 = large_mult(y, w), large_mult(y, z)
        return p1*10**(2*m) + (p2+p3)*10**m + p4

print('Devide & Conquer 알고리즘')
calculate_time(large_mult)
print()


# Karatsuba's Algorithm > 시간 복잡도: O(n**1.58) (=3*T(n/2)+cn = O(n**log_2^3))
# u = x * 10**m + y, v = w * 10**m + z
# r = (x + y) * (w + z) = xw + (xz + yw) + yz = p + (xz + yw) + q
# (xz + yw) = r - p - q
# uv = p*10**2m + (r-p-q)*10**m + q
def karatsuba(u, v):
    global threshold

    n = max(len(str(u)), len(str(v)))
    if u == 0 or v == 0:
        return 0
    elif n == threshold:
        return u * v
    else:
        m = n // 2
        x, y = u // 10**m, u % 10**m
        w, z = v // 10**m, v % 10**m
        p = karatsuba(x, w)
        q = karatsuba(y, z)
        r = karatsuba(x+y, w+z)
        return p*10**(2*m) + (r-p-q)*10**m + q

print("Karatsuba's Algorithm")
calculate_time(karatsuba)