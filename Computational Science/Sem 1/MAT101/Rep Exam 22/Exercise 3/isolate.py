import numpy as np

def my_isolate(M, t: int, e: int, s: str):
    rows, cols = M.shape
    N = np.zeros((rows, cols))
    
    if s == "close":
        for i in range(rows):
            for j in range(cols):
                if abs(M[i][j] - t) < e:
                    N[i][j] = M[i][j]
                else:
                    N[i][j] = 0
                    
        return N
    elif s == "far":
        for i in range(rows):
            for j in range(cols):
                if abs(M[i][j] - t) > e:
                    N[i][j] = M[i][j]
                else:
                    N[i][j] = 0
        
        return N
    else:
        raise ValueError("Invalid value for s")
    
    
def my_replace(v: list, t: int, e: int) -> list:
    w = []
    
    for ele in v:
        if abs(ele - t) < e:
            w.append(t)
        else:
            w.append(ele)
            
    return w

def replace(v, t, e):
    return [t if abs(x-t) < e else x for x in v]
    
if __name__ == "__main__":
    M = np.array([[1, 2, 3], [4, 5, 69], [7, 8, 9]])
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = 2
    e = 4
    print(my_isolate(M, t, e, "close"))
    print(my_isolate(M, t, e, "far"))
    print(my_replace(l, t, e))
    print(replace(l, t, e))
    