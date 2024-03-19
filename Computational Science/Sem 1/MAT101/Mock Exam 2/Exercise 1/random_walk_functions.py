# -*- coding: utf-8 -*-
# Author: Mert Erol
import random

def random_walk_recursive(steps):
    pos = 0
    if steps == 0:
        return 0
    else:
        if random.random() > 0.5:
            pos += 1
            random_walk_recursive(steps - 1)
        else:
            pos -= 1
            random_walk_recursive(steps - 1)
        
    return pos
        
def random_walk_iterative(steps):
    position = 0
    for _ in range(steps):
        # Generate a random number between 0 and 1 to decide the direction of the step.
        if random.random() < 0.5:  # Probability p = 0.5
            position += 1  # Move +1 step to the right
        else:
            position -= 1  # Move -1 step to the left
    return position

if __name__ == "__main__":
    print(random_walk_recursive(10))
    #print(random_walk_recursive(1000))
    
    print(random_walk_iterative(10))
    print(random_walk_iterative(1000))
