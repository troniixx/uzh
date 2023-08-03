#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def recursive_join(delim, values):
    
    if len(values) == 1:
        return values[0]
    else: return values[0] + delim + recursive_join(delim, values[1:])

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(recursive_join(" ", ["Hello", "world"]) == "Hello world")
assert(recursive_join(" <o> ", ["a", "b", "c"]) == "a <o> b <o> c")
assert(recursive_join("", ["a", "b", "c"]) == "abc")
assert("Your solution must be recursive!")