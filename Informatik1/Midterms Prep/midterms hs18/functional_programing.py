def double(x): return x*2

def app(list, op):

    output = []

    if len(list) == 0:
        return output

    for element in list:
        output.append(op(element))
    return output



print(app([], double))
print(app([1, 2, 3], double))
print(app([1, 2, 3], lambda x: x * 3))