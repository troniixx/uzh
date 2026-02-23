def foo_no_indent(a):
    result = None
    for item in a:
        if result == None:
            result = type(item)()
    
    result += item
    return result

def foo(a):
    result = None
    for item in a:
        if result == None:
            result = type(item)()
    
        result += item
    return result

print(foo([1, 2, 3]))
print(foo("hello"))
print(foo([[1, 2], [3, 4]]))