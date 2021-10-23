def find_sum(list, target):
    
    for idx1, v1 in enumerate(list):
        for idx2, v2 in enumerate(list):
            if idx1 == idx2:
                continue
            if v1 + v2 == target:
                return(idx1, idx2)
    return None


print(find_sum([], 9)) #None
print(find_sum([1], 2)) #None
print(find_sum([1, 1], 2)) #(0, 1)
print(find_sum([1, 7, 2, 11], 9)) #(1, 2)
print(find_sum([1, 2, 3, 4], 5)) #(0, 3)