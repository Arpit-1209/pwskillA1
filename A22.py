def set_intersection(set1, set2):
    return set1 & set2

set1 = {int(x) for x in input("Enter first set of integers: ").split(",")}
set2 = {int(x) for x in input("Enter second set of integers: ").split(",")}
print(set_intersection(set1, set2))
