def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value
    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))  # Output: {'a': 1, 'b': 5, 'c': 4}
