def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    prev_char = s[0]
    
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(prev_char + str(count))
            prev_char = char
            count = 1
    
    result.append(prev_char + str(count))
    return ''.join(result)

print(compress_string("aaabbc"))  # Output: "a3b2c1"
