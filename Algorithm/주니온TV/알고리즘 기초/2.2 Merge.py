def merge(U, V):
    S = []
    i = j = 0
    while i < len(U) and j < len(V):
        if U[i] < V[j] :
            S.append(U[i])
            i += 1
        else :
            S.append(V[j])
            j += 1
    if i < len(U):
        S += U[i:]
    else :
        S += V[j:]
    return S

def mergesort(S):
    n = len(S)
    if n <= 1 :
        return S
    else :
        mid = n // 2
        U = mergesort(S[0:mid])
        V = mergesort(S[mid:n])
        return merge(U, V)

def merge2(S, low, mid, high):
    U = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if S[i] < S[j] :
            U.append(S[i])
            i += 1
        else :
            U.append(S[j])
            j += 1
    if i <= mid:
        U += S[i:mid+1]
    else :
        U += S[j:high+1]
    for k in range(low, high+1):
        S[k] = U[k-low]
    return S

def mergesort2(S, low, high):
    if low < high :
        mid = (low + high) // 2
        mergesort2(S, low, mid)
        mergesort2(S, mid+1, high)
        print(S)
        merge2(S, low, mid, high)
    



S = [10, 9, 3, 5, 12, -1, 1]
print(mergesort(S))
mergesort2(S, 0, len(S)-1)
print(S)
