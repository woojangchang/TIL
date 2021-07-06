def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx


testAry = [62, 53, 10, 94]
minPos = findMinIdx(testAry)
print('최솟값 위치 :', minPos)
print('최솟값 :', testAry[minPos])