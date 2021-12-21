#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def dict_to_lists(d):
    keys = []
    values = []

    for (k, v) in d.items():
        keys.append(k)
        values.append(v)

    return (keys, values)


#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
x = {2: "b", 1: "a"}
l1, l2 = dict_to_lists(x)
assert(sorted(l1) == [1, 2])
assert(sorted(l2) == ["a", "b"])
assert(l2[1] == x[l1[1]])