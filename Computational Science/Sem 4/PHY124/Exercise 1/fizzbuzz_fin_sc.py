def fizz_buzz(n):
    result_list = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result_list.append("fizzbuzz")
        elif i % 3 == 0:
            result_list.append("fizz")
        elif i % 5 == 0:
            result_list.append("buzz")
        else:
            result_list.append(str(i))
            
    return ", ".join(result_list)

print(fizz_buzz(100))