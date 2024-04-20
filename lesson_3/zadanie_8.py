def duplicates(a):
    b = []
    for item in a:
        if item in b:
            return True
        b.append(item)
    return False
a = [1, 2, 3, 4, 5, 6, 7, 9, 9, 10]
if duplicates(a):
    print("Список содержит дубликаты.")
else:
    print("Список не содержит дубликатов.")