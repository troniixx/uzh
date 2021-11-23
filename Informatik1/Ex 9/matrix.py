#!/usr/bin/env python3
__author__ = "Mert Erol"
# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix
        # Implement this function and perform required checks
        # create adequate instance variables and check whether they should be private or public
        pass

    # To implement the required functionality, you will also have to implement two more
    # of the special functions that include a double underscore as per the task description.



    # DO NOT CHANGE the functions below! Consider also implementing __repr__ and __str__ for nice printing


    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))




# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    M = Matrix([[5,5],[5,5]])
    T = Matrix([[5,5],[5,5]])
    print(M)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)

