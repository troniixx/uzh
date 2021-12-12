#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def is_divisible_by(n, numbers):
	pass

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(is_divisible_by(30, [3, 6, 15]))
assert(not is_divisible_by(30, [3, 6, 29]))
try:
	is_divisible_by(30, [0, 6, 29])
	assert(False) # expected an exception!
except ValueError:
	pass # the correct exception was thrown

