SIZE = 5

# 큐 생성
queue = [None] * SIZE
front = rear = -1

# 삽입
rear += 1
queue[rear] = '삼색이'

rear += 1
queue[rear] = '야통이'

print(queue)

# 추출 (삭제)
front += 1
data = queue[front]
queue[front] = None
rear -= 1

print(data)
print(queue)