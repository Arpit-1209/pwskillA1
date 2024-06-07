def remove_element(lst, element):
    return [x for x in lst if x != element]

print(remove_element([1, 2, 3, 1, 4], 1))  # Output: [2, 3, 4]
