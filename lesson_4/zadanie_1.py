class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


a = Square(7)

print("Площадь квадрата:", a.area())

print("Периметр квадрата:", a.perimeter())