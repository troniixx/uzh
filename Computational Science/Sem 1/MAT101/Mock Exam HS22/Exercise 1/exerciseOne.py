import numpy as np
import math

def classifier(l, s):
    out = []
    
    if s == "positive":
        if all(isinstance(x, int) for x in l):
            for i in range(len(l)):
                if l[i] >= 0:
                    out.append(i)
                
        return out
    
    elif s == "negative":
        if all(isinstance(x, int) for x in l):
            for i in range(len(l)):
                if l[i] < 0:
                    out.append(i)
                
        return out
    
    else:
        raise ValueError("The string s must be either 'positive' or 'negative'.")
    
def matrixy(M, s, t):
    out = []
    i, j = M.shape
    
    if s == "bigger":
        for k in range(i):
            for l in range(j):
                if M[k, l] > t:
                    out.append((k, l))
        
        return out
    elif s == "smaller":
        for k in range(i):
            for l in range(j):
                if M[k, l] < t:
                    out.append((k, l))
        
        return out
    
    else:
        raise ValueError("The string s must be either 'bigger' or 'smaller'.")
    
def threesome(M):
    i, j, k = M.shape
    
    Q = np.zeros((i,j,k))
    
    for l in range(i):
        for m in range(j):
            for n in range(k):
                if M[l, m, n] > 0.5:
                    Q[l, m, n] = math.sqrt(M[l, m, n])
                elif M[l, m, n] <= 0.5 and M[l, m, n] >= -0.5:
                    Q[l, m, n] = M[l, m, n]
                else:
                    Q[l, m, n] = math.pow(M[l, m, n], 2)
                    
    return Q
    
if __name__ == "__main__":
    l = [1, 2, 3, -4, -5, 6, 7, 8, 9, 10]
    s = "positive"
    print(classifier(l, s))
    
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    s = "bigger"
    t = 5
    print(matrixy(M, s, t))
    
    s = "smaller"
    t = 5
    print(matrixy(M, s, t))
    
    M = np.random.rand(3, 3, 3)
    print(M)
    print("\n")
    print(threesome(M))