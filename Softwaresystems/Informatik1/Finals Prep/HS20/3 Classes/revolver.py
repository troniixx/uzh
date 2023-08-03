#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

import random

class Revolver:
    def __init__(self, cylinder_size):
        self.cylinder_size = cylinder_size
        self.reload()

    def reload(self):
        self.chamber = [True] + ([False] * (self.cylinder_size - 1))
        random.shuffle(self.chamber)

    def trigger(self):
        if self.chamber and self.chamber.pop():
            return "BANG!!!"
        return "Click!"

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