def reverse_list(lst):
    start, end = 0, len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

my_list = [1, 2, 3, 4]
reverse_list(my_list)
print(my_list)  # Output: [4, 3, 2, 1]
