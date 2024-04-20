def tablica(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")
number = int(input("Введите число для таблицы умножения: "))
print(f"Таблица умножения для числа {number}:")
tablica(number)