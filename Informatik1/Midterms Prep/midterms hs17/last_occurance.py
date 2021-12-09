def find_last_iterative(string, key):
    idx = -1
    for n in range(len(string)):
        if string[n] == key:
            idx = n
    
    return idx

def find_last_recursive(string, key):
    if string == None or string == "" or key not in string:
        return -1
    
    return 1 + find_last_recursive(string[1:], key)




print(find_last_iterative("The quick brown fox jumps over the lazy dog", "T"))
print(find_last_recursive("The quick brown fox jumps over the lazy dog", "T"))