def is_valid_encoding(a, b, mapping):
    if a == None and b == None:
        return True
    if a == "" and b == "":
        return True

    if a.translate(mapping) == b:
        return True
    else: return False

#assert(is_valid_encoding(None, None, {}))
#assert(is_valid_encoding(None, None, {'i': "don't care"}))
#assert(not is_valid_encoding(None, '', {}))
#assert(not is_valid_encoding('', None, {}))
assert(is_valid_encoding('cat', 'dog', {'c': 'd', 'a': 'o', 't': 'g'}))
assert(is_valid_encoding('a', 'archer', {'a': 'archer'}))
assert(is_valid_encoding('no', 'yes', {'n': 'y', 'o': 'es', 'z': 'z'}))