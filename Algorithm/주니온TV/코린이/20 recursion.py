def nCk(n,k):
    if k == 0 or n == k :
        return 1
    else :
        return nCk(n-1,k-1) + nCk(n-1, k)

for i in range(2,15):
    for j in range(i+1):
        print(nCk(i,j), end=' ')
    print()
