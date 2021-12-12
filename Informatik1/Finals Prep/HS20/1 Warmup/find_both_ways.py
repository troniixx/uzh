#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def find_both_ways(text, word):
    text = text.lower()
    word = word.lower()
    reverse = word[::-1]

    if word in text:
        return (True, 1)
    elif reverse in text:
        return (True, -1)
    else: return (False, 0)

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(find_both_ways("Hello, World!", "lo, wo") == (True, 1))
assert(find_both_ways("Hello, God!", "Dog") == (True, -1))
assert(find_both_ways("Hello, California!", "local") == (False, 0))