#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

import random

def lottery(values):
	draw = random.sample(range(1,51), k=len(values))
	# complete the implementation of this function

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
guess = [1,2,3,4,5]
res = lottery(guess)
assert(len(res[0]) == len(guess))
assert(res[1] in range(0,len(guess)+1))

