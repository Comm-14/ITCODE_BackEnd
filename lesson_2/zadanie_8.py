a = [1, 2, 3]
b = [4, 5, 6]
merged_list = a.copy()
merged_list.extend(b)
merged_list2 = a + b
print("Итоговые списки:", merged_list, merged_list2)