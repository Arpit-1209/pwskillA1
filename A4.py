def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True