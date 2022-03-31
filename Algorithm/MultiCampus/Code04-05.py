# 클래스, 함수 선언
class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current is None:
        print()
        return
    
    print(current.data, end=' ')
    printNodes(current.link)

    # while current.link:
    #     print(current.data, end=' ')
    #     current = current.link
    # print(current.data)

# 내가 짜본 insert 코드
def myinsertNode(position, data):
    global memory, head, current, pre
    if position == 0:
        node = Node()
        node.data = data
        node.link = head
        head = node
    
    else:
        current = head
        for _ in range(position):
            pre = current
            current = current.link
        node = Node()
        node.data = data
        node.link = current
        pre.link = node

    memory.append(node)

# 강의 insert 코드
def insertNode(findData, insertData):
    global memory, head, pre, current

    # 첫 데이터가 삽입할 위치 데이터인 경우
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # 삽입할 위치 데이터가 첫 데이터가 아닌 경우
    current = head
    while current.link:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    
    # 모든 노드를 다 훑었음에도 findData가 없는 경우, 마지막에 추가
    node = Node()
    node.data = insertData
    current.link = node

# 강의 delete Node
def deleteNode(deleteData):
    global memory, head, pre, current

    # 첫 데이터가 지울 데이터인 경우
    if head.data == deleteData:
        current = head
        head = current.link
        del(current)
        return
    
    # 지울 데이터가 첫 데이터가 아닌 경우(지울 데이터가 전체 데이터에 없는 경우)
    current = head
    while current.link:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
        

# 전역 변수부
memory = []
head, current, pre = None, None, None
dataArray = ['삼색이', '야통이', '길막이', '무', '래기']
# import random
# dataArray = [random.randint(1000, 9999) for _ in range(20)]


# 메인 코드부
if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
    
    printNodes(head)

    # myinsertNode(2, 10.1)
    insertNode('길막이', '뚱땅이')
    insertNode('래기', '빈집이')
    insertNode('haha ha', '연님이')
    printNodes(head)

    deleteNode('빈집이')
    deleteNode('haha ha')
    printNodes(head)
