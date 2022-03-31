def binarySearch(x, S):
    low = 0
    high = len(S)-1
    location = 0
    while (low <= high and location == 0):
        mid = (low+high) // 2
        if x == S[mid] :
            location = mid
        elif x < S[mid] :
            high = mid - 1
        else :
            low = mid + 1
    return location

x = 10
S = [0,1,2,3,4,5,6, 50, 60, 100]
print(binarySearch(x, S))
