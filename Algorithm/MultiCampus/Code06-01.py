# 스택 구조
stack = [None] * 5
top = -1

# push
top += 1
stack[top] = '삼색이'

top += 1
stack[top] = '야통이'

top += 1
stack[top] = '길막이'

for i in range(len(stack)-1, -1, -1):
    print(stack[i])
print()

# pop
data = stack[top]
print(data)
stack[top] = None
top -= 1

data = stack[top]
print(data)
stack[top] =  None
top -= 1
