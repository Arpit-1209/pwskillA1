def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return union, intersection, difference

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set_operations(set1, set2))  # Output: ({1, 2, 3, 4}, {2, 3}, {1})
