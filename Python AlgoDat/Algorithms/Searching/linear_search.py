def linearsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [12,45,78,98,63,21,458,78,96,420,69,21,78,96,55,266,10,666,214,789,654,1,2,4,8,9,3,5,78]
key = 10
print("element found at index "+str(linearsearch(arr,key)))