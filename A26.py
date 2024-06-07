def union_of_sets(set1, set2):
    return set1 | set2

set1 = {input("Enter first set of characters: ").split(",")}
set2 = {input("Enter second set of characters: ").split(",")}
print(union_of_sets(set1, set2))
