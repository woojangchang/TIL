def inner_product(a, b):
    import copy
    
    a = copy.deepcopy(list(a))
    b = copy.deepcopy(list(b))
    
    return sum([i * j for i, j in zip(a, b)])


def norm(a, l=2):
    return sum([abs(i) ** l for i in a]) ** (1/l)


def projection(b, a):
    """
    project vector `b` on `a` (parallel to a)
    """
    
    coef = inner_product(a, b) / inner_product(a, a)
    return [coef * i for i in a]



def outer_product(u, v):
    nrows = len(u)
    ncols = len(v)
    
    w = []
    
    for i in range(nrows):
        wrow = []
        for j in range(ncols):
            wrow.append(u[i] * v[j])
        
        w.append(wrow)
        
    return w



def cross_product(u, v):
    assert len(u) == len(v) == 3
    import copy
    u = copy.deepcopy(u)
    v = copy.deepcopy(v)
    
    w = []
    
    def determinant(A):
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    for i in range(3):
        sgn = (-1)**i
        m = [u[:i] + u[i+1:], v[:i] + v[i+1:]]
        w.append(sgn*determinant(m))
        
    return w