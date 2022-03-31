def subset (i, weight, total):
    n = len(w) - 1
    if promising(i, weight, total):
        if weight == W:
            for i in range(1, n+1) :
                if include[i] :
                    print(w[i], end=' ')
            print()
            #print(include[1:n+1])
        else:
            include[i+1] = True
            subset(i+1, weight+w[i+1], total-w[i+1])
            include[i+1] = False
            subset(i+1, weight, total - w[i+1])

def promising (i, weight, total):
    if (weight+total >= W ) and (weight == W or weight+w[i] <= W) :
        return True
    else :
        return False


w = [0, 5, 6, 10, 11, 16]
W = 21
include = [False] * len(w)

subset(0, 0, sum(w))
