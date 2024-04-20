def by_for(number):
    k = 0
    for a in str(number):
        if a.isdigit():
            k += 1
    return k
def by_while(number):
    k = 0
    while number > 0:
        k += 1
        number //= 10
    return k
number = int(input("Введите число: "))
print("Количество цифр (for цикл):", by_for(number))
print("Количество цифр (while цикл):", by_while(number))