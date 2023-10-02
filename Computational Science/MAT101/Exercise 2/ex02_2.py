def find_item(list, item):
    for idx in range(len(list)):
        if list[idx] == item:
            return idx
    return None

if __name__ == '__main__':
    L = [1, "abc", 1, 2, 2]
    
    print(find_item(L, 2))
    print(find_item(L, "abc"))
    print(find_item(L, 4))