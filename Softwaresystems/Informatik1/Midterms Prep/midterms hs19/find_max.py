def find_max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = find_max(list[1:])
        return m if m > list[0] else list[0]


m = [1, 2, 3, 10, 20, 30, 45, 12]
print(find_max(m))

