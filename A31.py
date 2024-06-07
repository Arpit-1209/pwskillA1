def word_frequencies(words):
    freqs = {}
    for word in words:
        freqs[word] = freqs.get(word, 0) + 1
    return freqs

print(word_frequencies(["apple", "banana", "apple", "apple", "banana", "cherry"]))
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}
