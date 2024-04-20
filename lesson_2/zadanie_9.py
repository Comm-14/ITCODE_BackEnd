list1 = [1, 2, 3, 4, 5]
list2 = [6, 5, 4, 7, 9]
list12 = list1 + list2
sorted = sorted(list12)
unique = []
for item in sorted:
    if item not in unique:
        unique.append(item)
print(unique)