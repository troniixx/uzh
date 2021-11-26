def is_valid_encoding(a, b, mapping):
    # If they're both exaclty None or empty, true.
    if a == b and (a == None or a == ''):
        return True
    # If one is None and the other empty, false.
    elif (a == None and b == '') or (a == '' and b == None):
        return False
    # Otherwise check bindings.
    else:
        tmp = ''.join([mapping.get(i, i) for i in a])
        return tmp == b

assert(is_valid_encoding(None, None, {}))
assert(is_valid_encoding(None, None, {'i': "don't care"}))
assert(not is_valid_encoding(None, '', {}))
assert(not is_valid_encoding('', None, {}))
assert(is_valid_encoding('cat', 'dog', {'c': 'd', 'a': 'o', 't': 'g'}))
assert(is_valid_encoding('a', 'archer', {'a': 'archer'}))
assert(is_valid_encoding('no', 'yes', {'n': 'y', 'o': 'es', 'z': 'z'}))