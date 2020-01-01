set1 = set(range(1, 7))
set2 = set(range(2, 11, 2))
set3 = set(range(1, 5))
print(set1, set2, set3)

print(set1 & set2) # intersection
print(set1 | set2) # union
print(set1 - set2) # difference
print(set1 ^ set2) # symmetricDifference
print(set2 <= set1) # <= subset
print(set3 <= set1)
print(set1 >= set2) # >= superset
print(set1 >= set3)