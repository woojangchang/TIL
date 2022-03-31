def partition(S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low+1, high+1):
        if S[i] < pivotitem :
            j += 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

def quicksort(S, low, high):
    if high > low :
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint-1)
        quicksort(S, pivotpoint+1, high)


def partition2(S, low, high):
    pivotitem = S[low]
    i = low +1
    j = high
    while i <= j :
        while i < high and S[i] < pivotitem :
            i += 1

        while j > low and S[j] > pivotitem :
            j -= 1

        if i < j :
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        #print(i, j, S, S[low:high+1])
        if i == j :
            break
    S[low], S[j] = S[j], S[low]
    #print(low, j, S, S[low:high+1])
    return i

def quicksort2(S, low, high):
    if high > low :
        pivotpoint = partition2(S, low, high)
        quicksort2(S, low, pivotpoint-1)
        quicksort2(S, pivotpoint, high)

#S = [15, 22, 13, 27, 12, 10, 20, 25]
#quicksort(S, 0, len(S)-1)
#print(S)

S2 = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
#S2 = [15, 22, 13, 27, 12, 10, 20, 25]

import time
x = time.time()
quicksort2(S2, 0, len(S2)-1)
print(S2)
print(time.time()-x)

S2 = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
x = time.time()
S2.sort()
print(S2)
print(time.time()-x)
