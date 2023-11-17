"""
PCL Exercise 5
Author: PCL Tutors
University of Zurich
Student Names: <your names>
"""


# Original code, do not change
def foobar():
    x = []
    for y in "I love solving exercises & getting them right! :)":
        if not y.isalnum():
            x.append(y)
    return x


# TODO: a.) Describe the code in natural language
#IT goes through all the characters in the string and checks if they are alphanumeric. If not, it appends them to the list x.
#including spaces

# TODO: b.) Rewrite the code using list comprehensions
def foobar_lc():
    return [y for y in "I love solving exercises & getting them right! :)" if not y.isalnum()]

# TODO: c.) Generalise the code to all strings, not just the one above
def get_nonalphanum(sentence):
    return [y for y in sentence if not y.isalnum()]

if __name__ == '__main__':
    print(foobar())
    print(foobar_lc())
    print(get_nonalphanum("The PCL Tutors are awesome! :-)"))