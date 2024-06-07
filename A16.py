def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

print(is_sorted([1, 2, 3]))  # Output: True
print(is_sorted([3, 2, 1]))  # Output: True
print(is_sorted([1, 3, 2]))  # Output: False
