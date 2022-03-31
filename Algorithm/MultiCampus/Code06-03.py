# 스택이 꽉 찼는지 확인하는 함수
def isStackFull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

# PUSH 함수
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('스택이 꽉 찼습니다.')
        return

    top += 1
    stack[top] = data

# 스택이 비었는지 확인하는 함수
def isStackEmpty():
    if top <= -1:
        return True
    else:
        return False

# POP 함수 (데이터 값을 리턴해야함)
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택이 비었습니다.')
        return
    
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 스택 초기화
SIZE = 5
stack = [None] * SIZE
top = -1

pop()
print(stack)

push('삼색이')
push('야통이')
push('길막이')
print(stack)

print(pop())
print(pop())
print(stack)