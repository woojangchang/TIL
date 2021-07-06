def factorial(num):
    if num <= 1:
        print(f'{num} 반환')
        return num
    print(f'{num}*{num-1}! 호출')
    retVal = factorial(num-1)

    print(f'{num}*{num-1}!(={retVal}) 반환')
    return num * retVal

n = 5
print(f'\n{n}! = {factorial(n)}')
    