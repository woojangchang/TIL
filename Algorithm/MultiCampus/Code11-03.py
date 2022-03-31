## 선택 정렬
## 함수 선언부
def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

## 전역 변수부
import random
dataAry = [random.randint(100, 190) for _ in range(8)]

## 메인 코드부
print('정렬 전 :', dataAry)

selectionSort(dataAry)

print('정렬 후 :', dataAry)