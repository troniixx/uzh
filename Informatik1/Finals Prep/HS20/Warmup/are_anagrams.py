#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def are_anagrams(a, b):
    a1 = []
    b1 = []
    
    for char in a:
        if char.isalpha():
            a1.append(char.lower())
    for char in b:
        if char.isalpha():
            b1.append(char.lower())

    a1.sort()
    b1.sort()

    return a1 == b1

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(are_anagrams('Dog', 'God'))
assert(are_anagrams("The Meaning of Life.", "The fine game of nil!"))
assert(not are_anagrams("The Meaning of Life", "Work"))