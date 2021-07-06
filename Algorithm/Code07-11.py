## 원형 큐 : 큐가 꽉 찬 것을 체크하기 위해 반드시 1칸을 남겨둔다.

## 함수 선언부

# 큐가 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, rear, front, queue
    if (rear+1)%SIZE == front:
        return True
    else:
        return False

# 큐에 데이터 삽입
def enQueue(data):
    global queue, rear
    if isQueueFull():
        print('큐가 꽉 찼습니다.')
        return
    rear = (rear+1)%SIZE
    queue[rear] = data

# 큐가 비었는지 확인하는 함수
def isQueueEmpty():
    global front, rear
    if front == rear:
        return True
    else:
        return False

# 큐에서 데이터 추출
def deQueue():
    global queue, front
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

## 전역 변수부

# 큐 초기화
SIZE = 5
queue = [None] * SIZE
front = rear = 0

## 메인 코드부
deQueue()

enQueue('삼색이')
enQueue('야통이')
enQueue('길막이')
enQueue('무')
enQueue('래기')
print(queue)

data = deQueue()
print(data)

data = deQueue()
print(data)

print(queue)

enQueue('뚱땅이')
enQueue('빈집이')
print(queue)

data = deQueue()
print(data)
print(queue)