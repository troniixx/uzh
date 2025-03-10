import numpy as np

def filter(seq, ignore):
    return [x for x in seq if x not in ignore]

def find(seq, val):
    return [i for i, x in enumerate(seq) if x == val]

def common(seq1, seq2):
    return list(set(seq1) & set(seq2))

print(filter(np.array([6, 9, 3, 7, 4, 2, 4, 7, 9, 8, 10]), [2]))
print(find((2, 4, 8, 9, 8, 5, 1, 9, 8, 3, 4), 2))
print(find([7.5, 0.9, 0.6, 8.2, 6.5, 9.5, 0.9, 9.3, 5.1, 1.8], 0.9))
print(common([2, 4, 8, 9, 8, 5, 1, 9, 8, 3, 4], [6, 9, 3, 7, 4, 2, 4, 7, 9, 8, 10]))


l1 = [26, 39, 19, 33, 38, 76, 45, 22, 98, 84, 81, 83, 11, ' ', ' ', 79, 70, 87, 18, 48, 97, 88, ' ']
l2 = [97, 39, 24, 70, ' ', 41, 85, 17, 58, 15, 16, 60, 26, 56, 66, 62, 61, ' ', 84, ' ', 14, 78, 54]
ig = [" ", ""]

cleaned1 = filter(l1, ig)
cleaned2 = filter(l2, ig)

intersec = common(cleaned1, cleaned2)
max_common = max(intersec)

indexes_l1 = find(l1, max_common)
indexes_l2 = find(l2, max_common)

print(indexes_l1, indexes_l2)