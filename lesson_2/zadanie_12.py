string = input("Введите числа, разделенные запятой: ")
numbers = string.split(',')
numbers_list = [int(num) for num in numbers]
numbers_tuple = tuple(numbers_list)
print("Список чисел:", numbers_list)
print("Кортеж чисел:", numbers_tuple)