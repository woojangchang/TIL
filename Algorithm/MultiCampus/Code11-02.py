## 함수 선언부
def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

def findMaxIdx(ary):
    maxIdx = 0
    for i in range(1, len(ary)):
        if ary[maxIdx] < ary[i]:
            maxIdx = i
    return maxIdx

## 전역 변수부
import random
# before = [random.randint(100, 190) for _ in range(8)]
# ord('가') : 44032, ord('힣') : 55203 이용
before = [chr(random.randint(44032, 55203)) for _ in range(30)]
after = []

## 메인 코드부
print('정렬 전 :', before)

for _ in range(len(before)):
    # minPos = findMinIdx(before)
    # after.append(before[minPos])
    # del(before[minPos])
    maxPos = findMaxIdx(before)
    after.append(before[maxPos])
    del(before[maxPos])

print('정렬 후 :', after)