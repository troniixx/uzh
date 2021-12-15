def recursive_join(delim, values):
    if len(values) == 1:
        return values[0]
    else: return values[0] + delim + recursive_join(delim, values[1:])
    

# DO NOT SUBMIT THE LINES BELOW!
assert(recursive_join(" ", ["Hello", "world"]) == "Hello world")
assert(recursive_join("  ", ["a", "b", "c"]) == "a  b  c")
assert(recursive_join("", ["a", "b", "c"]) == "abc")
assert("Your solution must be recursive!")