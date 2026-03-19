#/usr/bin/python3

class VectorClock(object):

    # initialization 
    def __init__(self):
        self.clock = {}  # node => counter

    # turn to string    
    def __str__(self):
        return "{%s}" % ", ".join(["%s:%d" % (node, self.clock[node])
                                    for node in sorted(self.clock.keys())])

    # update
    def update(self, node, counter):
        """Add a new node:counter value to a VectorClock."""
        
        
    #comparison
    def __eq__(self, other):
        return self.clock == other.clock

        
    def __lt__(self, other):
        return all(self.clock[node] < other.clock[node] for node in self.clock)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass
    
    #reconcile (if possible, otherwise return error)
    def reconcile(self, other):
        pass


            
            
        
