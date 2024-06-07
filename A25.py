def slice_tuple(t, start, end):
    return t[start:end+1]

print(slice_tuple((1, 2, 3, 4, 5), 1, 3))  # Output: (2, 3, 4)
