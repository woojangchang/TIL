# 이진 탐색 : 정렬된 array에 사용가능한 빠른 탐색 방법

# 내가 짠 코드
def binarySearch(start, end, findData, ary):
    mid = (start + end) // 2
    if ary[mid] == findData:
        return mid
    elif start == end:
        return -1
    elif ary[mid] < findData:
        return binarySearch(mid+1, end, findData, ary)
    else:
        return binarySearch(start, mid-1, findData, ary)

# 강의 코드
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1

    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid+1
        else:
            end = mid-1
    return pos

ary = [12, 23, 25, 52, 98, 122, 162, 190, 222, 521, 1995]
idx = binarySearch(0, len(ary)-1, 52, ary)
print(idx)
idx = binarySearch(0, len(ary)-1, 100, ary)
print(idx)

idx = binSearch(ary, 52)
print(idx)
idx = binSearch(ary, 100)
print(idx)
