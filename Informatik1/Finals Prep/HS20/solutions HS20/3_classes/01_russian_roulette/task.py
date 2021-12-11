#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

import random

class Revolver:
	pass

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
gun = Revolver(6)
turns = [gun.trigger() for i in range(10)]
assert("BANG!!!" in turns[0:6])
assert("BANG!!!" not in turns[6:])
gun.reload()
turns = [gun.trigger() for i in range(10)]
assert("BANG!!!" in turns[0:6])
assert("BANG!!!" not in turns[6:])

