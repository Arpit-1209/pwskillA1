def get_nested_value(d, keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d

nested_dict = {"a": {"b": {"c": 1}}}
print(get_nested_value(nested_dict, ["a", "b", "c"]))  # Output: 1
print(get_nested_value(nested_dict, ["a", "b", "d"]))  # Output: None
