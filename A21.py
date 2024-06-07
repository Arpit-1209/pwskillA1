def common_elements(t1, t2):
    return tuple(set(t1) & set(t2))

print(common_elements((1, 2, 3), (2, 3, 4)))  # Output: (2, 3)
