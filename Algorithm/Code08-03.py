## 함수, 클래스 선언부
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


## 전역 변수부
memory = []
root = None
nameAry = ['무', '길막이', '삼색이', '야통이', '연님이', '래기']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right
    memory.append(node)

# 데이터 검색
findName = '래기'
current = root
while True:
    if current.data == findName:
        print(findName)
        break
    elif findName < current.data:
        if current.left is None:
            print('데이터 없음')
            break
        print(current.data)
        current = current.left
    else:
        if current.right is None:
            print('데이터 없음')
            break
        print(current.data)
        current = current.right
