class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def delit(self):
        return self.a / self.b
    def umnogit(self):
        return self.a * self.b

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
calculate = Calculate(a ,b)
k = int(input("Выберите действие(1 - Сложить, 2 - Вычесть, 3 - Поделить, 4 - Умножить): "))
if k == 1:
    print("Сумма:", calculate.plus())
elif k == 2:
    print("Разность:", calculate.minus())
elif k == 3:
    print("Деление:", calculate.delit())
elif k == 4:
    print("Произведение:", calculate.umnogit())