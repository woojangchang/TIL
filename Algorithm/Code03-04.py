# 데이터 추가
def add_data(friend):

    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

# 데이터 삽입
def insert_data(position, friend):
    kLen = len(katok)
    if position > kLen:
        return
    
    katok.append(None)
    for i in range(kLen, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

# 데이터 삭제
def delete_data(position):
    kLen = len(katok)
    if position > kLen-1:
        return

    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

if __name__ == '__main__':
    katok = []
    cmd = int(input('1-추가, 2-삽입, 3-삭제, 4-종료 : '))
    while cmd != 4 :
        if cmd == 1 :
            friend = input('추가할 이름 입력 : ')
            add_data(friend)
        elif cmd == 2 :
            position, friend = input('삽입할 위치와 이름 입력 : ').split()
            position = int(position)
            insert_data(position, friend)
        elif cmd == 3 :
            position = int(input('삭제할 위치 입력 : '))
            delete_data(position)
        else :
            print('1~4 입력')
            
        print(katok)
        cmd = int(input('1-추가, 2-삽입, 3-삭제, 4-종료 : '))
        