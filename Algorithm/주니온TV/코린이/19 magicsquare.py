def new_row(k, n):
    if k == -1 :
        return n-1
    elif k == n :
        return 0
    else :
        return k

def new_col(k, n):
    if k == -1 :
        return n-1
    elif k == n :
        return 0
    else :
        return k

def makeMagicSquare(n):
    if n % 2 == 0 :
        print("Can't make Magic Square with size {}x{}".format(n,n))
    else :
        square = [[0]*n for _ in range(n)]
        row = 0
        col = n // 2
        for k in range(1, n*n+1):
            square[row][col] = k
            tmp_row = new_row(row-1, n)
            tmp_col = new_col(col-1, n)
            if square[tmp_row][tmp_col] != 0 :
                row = new_row(row+1, n)
            else :
                row = tmp_row
                col = tmp_col
        return square


def checkMagic(square):
    magic = 0
    for i in range(len(square)):
        magic += square[0][i]
    for i in range(len(square)):
        rsum = 0
        csum = 0
        for j in range(len(square)):
            rsum += square[i][j]
            csum += square[j][i]

        if rsum != magic or csum != magic :
            return False

    dsum = 0
    d2sum = 0
    for d in range(len(square)):
        d2 = len(square) - 1 - d
        dsum += square[d][d]
        d2sum += square[d2][d]

    if dsum != magic or d2sum != magic :
        return False
    return True

makeMagicSquare(2)
for i in [3,5,7] :
    magicsquare = makeMagicSquare(i)
    for row in magicsquare :
        print(row)
    print(checkMagic(magicsquare))
