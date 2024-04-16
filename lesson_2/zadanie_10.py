import random
def unique(a):
    return len(set(a)) == len(a)

# Пример последовательности
n = 6
a = [random.randint(1,9) for i in range(n)]
print(a)
result = unique(a)
print("Все числа уникальны?" , result)