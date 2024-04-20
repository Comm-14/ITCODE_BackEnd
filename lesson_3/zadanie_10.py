def reversedd(variable):
    res=''.join(reversed(variable))
    return res
n = reversedd(input("Введите строку:"))
print("Обратная строка", n)