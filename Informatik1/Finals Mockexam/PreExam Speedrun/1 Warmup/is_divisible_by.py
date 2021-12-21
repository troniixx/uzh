#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def is_divisible_by(n, numbers):

    if not numbers or 0 in numbers:
        raise ValueError
    
    for num in numbers:
        if n % num != 0:
            return False
    return True

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(is_divisible_by(30, [3, 6, 15]))
assert(not is_divisible_by(30, [3, 6, 29]))
try:
    is_divisible_by(30, [0, 6, 29])
    assert(False) # expected an exception!
except ValueError:
    print( "Well Done") # the correct exception was thrown