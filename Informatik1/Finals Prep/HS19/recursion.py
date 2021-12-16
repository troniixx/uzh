class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
    
root = Node(10, \
    Node(5, Node(3), Node(18)), \
    Node(15, Node(8)))

def range_sum(node, lower, upper):
    res = 0
    if lower <= node.v < upper:
        res += node.v
    if node.l != None:
        res += range_sum(node.l, lower, upper)
    if node.r != None:
        res += range_sum(node.r, lower, upper)
    
    return res

assert range_sum(Node(7), 1, 100) == 7
assert range_sum(Node(2, Node(3, Node(4))), 2, 4) == 5
assert range_sum(root, 4, 10) == 13 # see example above