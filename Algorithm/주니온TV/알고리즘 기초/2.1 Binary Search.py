def location(S, low, high, x):
    if (low > high) :
        return 0
    else :
        mid = (low+high) // 2
        if x == S[mid] :
            return mid
        elif x < S[mid] :
            return location(S, low, mid-1, x)
        else :
            return location(S, mid+1, high, x)

S = [1, 3, 5, 7, 11, 12, 13, 15]
x = 14
print(location(S, 0, len(S)-1, x))
