def has_unique_characters(s):
    return len(set(s)) == len(s)

print(has_unique_characters("abcdef"))  # Output: True
print(has_unique_characters("hello"))   # Output: False
