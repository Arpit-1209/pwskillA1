def find_all_occurrences(s, sub):
    start = 0
    indices = []
    while start < len(s):
        start = s.find(sub, start)
        if start == -1:
            break
        indices.append(start)
        start += 1  # Move past this match
    return indices

# Example usage
string = "abracadabra"
substring = "abra"
print(find_all_occurrences(string, substring))  # Output: [0, 7]
