def count_occurrences(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

print(count_occurrences([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}
