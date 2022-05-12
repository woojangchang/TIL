# 유클리드 호제법 이용
# gcd(x, y) = gcd(y, x%y)

def gcd(x:int, y:int):
    assert x>y, "x must be bigger than y"
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

x, y = 78696, 19332
print(gcd(x, y))


def lcm(x:int, y:int):
    return x*y//gcd(x,y)

print(lcm(x, y))


def is_relatively_prime(x, y):
    return gcd(x, y)==1

print(is_relatively_prime(1234, 987))