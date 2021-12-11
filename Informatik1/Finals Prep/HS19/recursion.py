class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
    
root = Node(10, \
    Node(5, Node(3), Node(18)), \
    Node(15, Node(8)))

def range_sum(node, lower, upper):
    sum = 0
    