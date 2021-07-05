# 노드 생성
class Node:
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '삼색이'

node2 = Node()
node2.data = '야통이'
node1.link = node2

node3 = Node()
node3.data = '길막이'
node2.link = node3

node4 = Node()
node4.data = '무'
node3.link = node4

node5 = Node()
node5.data = '래기'
node4.link = node5

# 출력
current = node1
while current.link:
    print(current.data, end=' ')
    current = current.link
print(current.data)

# 노드 삽입
new_node = Node()
new_node.data = '뚱땅이'
new_node.link = node2.link
node2.link = new_node

current = node1
while current.link:
    print(current.data, end=' ')
    current = current.link
print(current.data)

# 노드 삭제
node2.link = new_node.link
del(new_node)

current = node1
while current.link:
    print(current.data, end=' ')
    current = current.link
print(current.data)