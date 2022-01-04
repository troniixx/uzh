def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [12,45,78,98,63,21,458,78,96,420,69,21,78,96,55,266,666,214,789,654,1,2,4,8,9,3,5,78]

bubble_sort(arr)
print("Sorted array is: ")
print(arr)