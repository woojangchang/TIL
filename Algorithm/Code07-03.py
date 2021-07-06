# 큐가 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, rear, front, queue
    # 빈칸(None)이 뒤쪽에 있는 경우
    if rear != SIZE-1:
        return False

    # 빈칸(None)이 뒤쪽에 없고, 앞에도 꽉찬 경우
    elif (rear >= SIZE-1) and (front==-1):
        return True

    # 빈칸(None)이 앞쪽에 있는 경우, 앞으로 한 칸씩 땡김
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# 큐에 데이터 삽입
def enQueue(data):
    global queue, rear
    if isQueueFull():
        print('큐가 꽉 찼습니다.')
        return
    rear += 1
    queue[rear] = data

# 큐가 비었는지 확인하는 함수
def isQueueEmpty():
    global front, rear
    if front >= rear:
        return True
    else:
        return False

# 큐에서 데이터 추출
def deQueue():
    global queue, front
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 큐 초기화
SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1

deQueue()

enQueue('삼색이')
enQueue('야통이')
enQueue('길막이')
print(queue)

data = deQueue()
print(data)

data = deQueue()
print(data)

print(queue)

enQueue('무')
enQueue('래기')
print(queue)

print(deQueue())
print(deQueue())
print(deQueue())
print(queue)

enQueue('뚱땅이')
print(queue)
enQueue('빈집이')
print(queue)