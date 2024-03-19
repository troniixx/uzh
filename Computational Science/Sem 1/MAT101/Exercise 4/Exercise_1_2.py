#Homework_4_Exercise_1

def factorial(num):
    """
    Returns the factorial of "num".

    Prints a warning and returns None if "num" is negative or not an int.
    
    Input:
        num: int

    Output:
        result: int
    """
    # making sure "num" is an int
    if type(num) is not int:
        print("Parameter 'num' as value '" + str(num)
            # NOTE indent error below
            + "' of type " + str(type(num)) + " but should be of type int.")
        return None

    # making sure "num" is positive
    if num < 0:
        print("Parameter 'num' as value '" + str(num)
            # NOTE indent error below
            + "' but should be positive.")
        return None

    # preceeding to calculate num!
    result = 1 # defining the output variable
    
    # multiply result with every integer between "num" and 0
    
    while num > 1: # NOTE changed 10 to 1
        result = result*num
        num = num - 1

    # returning the result
    return result


def sum_list(array):
    """
    Returns the sum of all ints and floats in the list "array".
    Elements of other types are ignored.

    Prints a warning and returns 0 if "array" is not of type list.
    Returns 0 if "array" is empty or contains no ints or floats.

    Input:
        array: list

    Output:
        result: float
    """
    # making sure "array" is a list
    if type(array) is not list:
        print("Parameter 'array' as value '" + str(array) + "' of type "
            + str(type(array)) + " but should be of type list.")
        return None
    
    result = 0

    # calculating the sum over "array"
    for index in range(0, len(array)): # NOTE changed range from (1, len(array)) to (0, len(array)
        
        # getting the next element in the list
        element = array[index]

        # need to skip elements that are neither int nor float
        if type(element) in [int, float]:
            # adding valid elements to the result
            result += element

    # returning the result
    return result    




if __name__ == "__main__":
    #print("Factorial:\n")
    #print(factorial(5)) #no output at all, should return 120
    #print(factorial(0)) #no output at all, should return 1
    #print(factorial(1)) #no output at all, should return 1
    #print(factorial(-5)) #correct output
    #print(factorial(5.5)) #correct output
    #print(factorial("hello")) #correct output
    #print(factorial([])) #correct output
    #print(factorial([1, 2, 3, 4, 5])) #correct output

    #print("Sum list:\n")
    #print(sum_list([1, 2, 3, 4, 5])) #wrong output, should return 15 instead of 14
    #print(sum_list([1, 2, 3, "hello", 4, 5])) #wrong output, should return 15 instead of 14
    #print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #wrong output, should return 55 instead of 54
    #print(sum_list("hello")) #correct output
    #print(sum_list(5)) #corect
    #print(sum_list([])) #correct output
    
    
    #Homework_4_Exercise_2
    user_input = input("Enter a list of numbers separated by spaces: ") #NOTE removed extra bracket
    numbers = user_input.split()
    
    #NOTE added int() to the list comprehension in the second part
    #NOTE changed the if statement == 1 to == 0
    even_numbers = [int(x) for x in numbers if int(x) % 2 == 0]
    squared_numbers = [x*2 for x in even_numbers]
    
    #NOTE added this to check if there are any squared numbers to avoid division by zero
    if len(squared_numbers) > 0:
        avg_of_squares = sum(squared_numbers) / len(squared_numbers)
        print(f"The average of squared even numbers is: {avg_of_squares}")
    else:
        print("No even numbers were entered or there has been a division by zero.")