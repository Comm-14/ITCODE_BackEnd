def remove_by_for_and_pop(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)-1):
            if a[i] == a[j]:
                a.pop(j)
    if a[len(a) -1] == a[len(a) -2]:
        a.pop(len(a) - 1)
def remove_by_while_and_del(a):
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                del a[j]
            else:
                j += 1
        i += 1

# Пример использования
b = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10]
print("Исходный список:", b)
b1 = b
# Удаление дубликатов с использованием pop() и for
remove_by_for_and_pop(b1)  # Копируем список, чтобы не изменять оригинал
print("Без дубликатов (pop() и for):", b1)
b2 = b
# Удаление дубликатов с использованием del и while
remove_by_while_and_del(b2)  # Копируем список, чтобы не изменять оригинал
print("Без дубликатов (del и while):", b2)