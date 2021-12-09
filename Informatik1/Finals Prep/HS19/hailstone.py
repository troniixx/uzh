def hail_me_daddy(num):
    res = []
    res.append(int(num))

    while num != 1:
        if num%2 == 0:
            num = num/2
            res.append(int(num))
        else:
            num = 3*num + 1
            res.append(int(num))
    
    return res

print(hail_me_daddy(12))