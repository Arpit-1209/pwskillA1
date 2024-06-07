def difference_of_sets(set1, set2):
    return set1 - set2

set1 = {input("Enter first set of strings: ").split(",")}
set2 = {input("Enter second set of strings: ").split(",")}
print(difference_of_sets(set1, set2))
