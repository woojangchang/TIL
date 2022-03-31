def aratorome(n):
    rome = ''
    if n // 1000 != 0 :
        rome += 'M' * (n // 1000)
    n = n % 1000

    if n // 100 == 9 :
        rome += 'CM'
    elif n // 100 >= 5 :
        rome += 'D' + 'C'*(n//100 - 5)
    elif n // 100 == 4 :
        rome += 'CD'
    elif n // 100 > 0 :
        rome += 'C' * (n//100)
    n = n % 100

    if n // 10 == 9 :
        rome += 'XC'
    elif n // 10 >= 5 :
        rome += 'L' + 'X'*(n//10 - 5)
    elif n // 10 == 4 :
        rome += 'XL'
    elif n // 10 > 0 :
        rome += 'X' * (n//10)

    n = n % 10

    if n % 10 == 9 :
        rome += 'IX'
    elif n % 10 >= 5 :
        rome += 'V' + 'I'*(n%10 - 5)
    elif n % 10 == 4 :
        rome += 'IV'
    elif n % 10 > 0 :
        rome += 'I' * (n%10)

    return rome

for i in [369, 80, 29, 155, 14, 492, 348, 301, 469, 499] :
    print(aratorome(i), end=', ')
