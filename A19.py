def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

print(union([1, 2, 3], [2, 3, 4]))  # Output: [1, 2, 3, 4]
