a = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
for index, element in enumerate(a, start=1):
    if index % 3 == 0:
        print(f"Индекс: {index}, Элемент: {element}")