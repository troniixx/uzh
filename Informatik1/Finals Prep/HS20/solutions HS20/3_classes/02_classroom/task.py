#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

class Classroom:
	pass

class Student:
	pass

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
s1 = Student("Alice", "Bauer")
s2 = Student("Jack", "Wonderland")
assert(s1.matno == 0)
assert(s2.matno == 1)
c = Classroom()
c.add(s1)
c.add(s2)
assert(len(c.students) == 2)
c.remove(s2.matno)
assert(len(c.students) == 1)
try: # adding a student already in c
	c.add(s1)
	assert(False) # expected a ValueError!
except ValueError:
	pass # the correct exception has been thrown
try: # removing a student not in c
	c.remove(s2.matno)
	assert(False) # expected a ValueError!
except IndexError:
	pass # the correct exception has been thrown

