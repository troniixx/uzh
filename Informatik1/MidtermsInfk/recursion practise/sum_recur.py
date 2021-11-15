def sum(nlist):
    if len(nlist) == 1:
        return nlist[0] 
    else:
        return nlist[0] + sum(nlist[1:])

print(sum(([1, 2, 3, 4, 5])))
