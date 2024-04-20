# Используем цикл for
def sum_for(n):
    a = 0
    for i in range(2, n+1, 2):
        a += i
    return a
# Используем цикл while
def sum_while(n):
    b = 0
    i = 2
    while i <= n:
        b += i
        i += 2
    return b
n = 14
result_for = sum_for(n)
result_while = sum_while(n)

print(f"Сумма всех четных чисел от 1 до {n} (с использованием цикла for) : {result_for}")
print(f"Сумма всех четных чисел от 1 до {n} (с использованием цикла while) : {result_while}")