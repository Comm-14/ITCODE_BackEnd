from datetime import datetime
class Human:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year


human = Human('Дамир', 'Уфа', 2003)
print(f"Возраст: {human.name} {human.age()}")