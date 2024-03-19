# -*- coding: utf-8 -*-
# Author: Mert Erol, 20-915-245

import numpy as np
from numpy.typing import NDArray

# a)
def is_bigger(v: list | NDArray[np.float64], t: int) ->  list:
    res = []
    
    for idx, value in enumerate(v): # Iterate over the vector
        if value > t: # Check if the element is bigger than the threshold
            res.append(idx) # Append the index to the list
    
    return res


# b)
def average_rows(m: list | NDArray[np.float64]) -> NDArray[np.float64]:
    averages = []  # A list to store the averages

    for row in m:
        row_sum = np.sum(row)  # Sum the elements in the row
        row_average = row_sum / len(row)  # Calculate the average
        averages.append(row_average)  # Append the average to the list

    return np.array(averages)

if __name__ == "__main__":
    # a)
    v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t = 5
    print(is_bigger(v, t))
    
    # b)
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(average_rows(m))