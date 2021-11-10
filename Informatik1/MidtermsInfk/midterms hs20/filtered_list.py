# list_reversed_filtered([1,2,3,4,5], [1,3]) should return [5,4,2]
def list_reversed_filtered(l1, l2):
    spinnyboy = l1[::-1]
    res = []

    for n in spinnyboy:
        if n not in l2:
            res.append(n)
    

    return res

if __name__ == '__main__':
    print(list_reversed_filtered([1,2,3,4,5], [1,3]))

