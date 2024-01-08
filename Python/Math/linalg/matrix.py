import numpy as np
from .vector import inner_product

def determinant(A):
    """
    Paramters
    ---------
    A: n x n 행렬 (list 또는 numpy ndarray)
    
    
    Returns
    -------
    determenant of A (float)
    """
    
    nrows = len(A)
    ncols = len(A[0])
    
    assert nrows == ncols, f'nrows ({nrows}) != ncols ({ncols})'
    
    import copy
    
    A = copy.deepcopy(A)
    if isinstance(A, np.ndarray):
        A = A.tolist()
    
    if nrows == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    
    det = 0
    for i in range(ncols):
        sgn = (-1) ** (i%2)
        Aii = [A[j][0:i] + A[j][i+1:] for j in range(1, ncols)]
        det += sgn * A[0][i] * determinant(Aii)
        
    return det



def Cofactor(A):
    """
    A: 3 x 3 이상인 행렬
    """
    import copy
    
    A = copy.deepcopy(A)
    if isinstance(A, np.ndarray):
        A = A.tolist()
    
    nrows = len(A)
    ncols = len(A[0])
        
    C = []
    
    for i in range(nrows):
        Ci = []
        for j in range(ncols):
            Aij = [A[k][:j] + A[k][j+1:] for k in range(nrows) if k != i]
            Cij = (-1)**(i+j) * determinant(Aij)
            
            Ci.append(Cij)
        
        C.append(Ci)
    
    return C



def transpose(A):
    """
    A^T
    """
    import copy
    
    A = copy.deepcopy(A)
    if isinstance(A, np.ndarray):
        A = A.tolist()

    nrows = len(A)
    ncols = len(A[0])
    
    AT = []
    for j in range(ncols):
        AT_row = []
        
        for i in range(nrows):
            AT_row.append(A[i][j])
            
        AT.append(AT_row)
        
    return AT




def inverse(A):
    import copy
    
    A = copy.deepcopy(A)
    if isinstance(A, np.ndarray):
        A = A.tolist()
    
    nrows = len(A)
    ncols = len(A[0])
    
    det = determinant(A)
    assert det != 0, "det(A) != 0"
    
    
    if nrows == 2:
        return [[A[1][1] / det, -A[0][1] / det], [-A[1][0] / det, A[0][0] / det]]
    
    adjA = transpose(Cofactor(A))
    
    invA = []
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(adjA[i][j] / det)
            
        invA.append(row)
        
    return invA



def add_matrix(A, B):
    import copy
    
    X = copy.deepcopy(A)
    Y = copy.deepcopy(B)
    
    if isinstance(X, np.ndarray):
        X = X.tolist()
    
    if isinstance(Y, np.ndarray):
        y = y.tolist()
        
    
    assert len(X) == len(Y)
    assert len(X[0]) == len(Y[0])
    
    Z = []
    
    for xrow, yrow in zip(X, Y):
        zrow = []
        for xcol, ycol in zip(xrow, yrow):
            zrow.append(xcol + ycol)
            
        Z.append(zrow)
        
    return Z



def multiple_matrix(A, b):
    """
    A: m x n matrix
    b: n x k matrix
    """
    import copy
    
    X = copy.deepcopy(A)
    y = copy.deepcopy(b)
    
    if isinstance(X, np.ndarray):
        X = X.tolist()
    
    if isinstance(y, np.ndarray):
        y = y.tolist()
        
    ncols = len(X[0])
    nrows = len(y)
    
    assert ncols == nrows
    
    Z = []
    
    if not isinstance(y[0], list): # k = 1
        for row in X:
            element = 0
            for j in range(ncols):
                element += row[j] * y[j]
            
            Z.append(element)
        
        return Z
    
    
    for i, row in enumerate(X):
        zrow = []
        for k in range(len(y[0])):
            element = 0
            
            for j in range(ncols):
                element += row[j] * y[j][k]
                
            zrow.append(element)
            
        Z.append(zrow)
        
    return Z




def solve_linalg(A, b):
    """
    연립 방정식 풀기
    입력값: 솔루션을 구하고 싶은 A, b
    출력값: 방정식의 솔루션 sol
    """
    Ainv = inverse(A)
    
    return multiple_matrix(Ainv, b)


def normalize(a):
    square_sum = 0
    for i in a:
        square_sum += i ** 2
    square_sum **= 0.5
    
    return [i / square_sum for i in a]


def orthogonal_basis(X):
    Xt = transpose(X)
    
    Vt = [Xt[0]]
    
    for i, xi in enumerate(Xt[1:], start=1):
        vi = xi[:]
        for vj in Vt:
            coef = inner_product(xi, vj) / inner_product(vj, vj)
            vi = [vii - coef * vji for vii, vji in zip(vi, vj)]
        Vt.append(vi)
        
    Vt = [normalize(vt) for vt in Vt]
            
    return transpose(Vt)



def qr_decomposition(A):
    import copy
    A = copy.deepcopy(A)
    
    Q = orthogonal_basis(A)
    Qt = transpose(Q)
    R = multiple_matrix(Qt, A)
    return Q, R



def eye(n, mul=1):
    I = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I[i][j] = 1 * mul
    return I




def eigenvalues(A, iterations=10000, tol=1e-4):
    import copy
    Ak = copy.deepcopy(A)
    n = len(A)
    
    Uk = eye(n)
    for k in range(iterations):
        Qk, Rk = qr_decomposition(Ak)
        Ak = multiple_matrix(Rk, Qk)
        Ukafter = multiple_matrix(Uk, Qk)
        
        diff = 0
        for urow, uarow in zip(Uk, Ukafter):
            diff_row = sum([abs(u-ua) for u, ua in zip(urow, uarow)])
            diff += diff_row
            
        if diff < tol:
            break
            
        Uk = Ukafter
    
    return [Ak[i][i] for i in range(n)]