list1 = [1, 2, 3, 4, 5]
list2 = [6, 5, 4, 7, 9]
combined = list1 + list2
sorted = sorted(combined)
unique = []
for item in sorted:
    if item not in unique:
        unique.append(item)
print(unique)