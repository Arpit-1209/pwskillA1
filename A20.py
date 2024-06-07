import random

def shuffle_list(lst):
    result = lst[:]
    random.seed(0)  # For reproducibility
    for i in range(len(result) - 1, 0, -1):
        j = random.randint(0, i)
        result[i], result[j] = result[j], result[i]
    return result

print(shuffle_list([1, 2, 3, 4, 5]))  # Output will vary
