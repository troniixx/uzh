def reverse(array):
    if not isinstance(array, list): 
        print(TypeError("Input must be a list"))
        return None
    
    new_list = []
    for item in range(len(array)-1, -1, -1):
        new_list.append(array[item])
    
    return new_list

def reverse_inplace(array):
    if not isinstance(array, list): 
        print(TypeError("Input must be a list"))
        return None
    
    array.reverse()

if __name__ == '__main__':
    array1 = [1, 2, 3]
    rev_array = reverse(array1)
    print(rev_array)    
    print(array1)
    array2 = [1, 2, 3, 4]
    reverse_inplace(array2)
    print(array2)