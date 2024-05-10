class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать.")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} ест.")
        self.power += 1

    def hit(self):
        print(f"{self.name} наносит удар.")
        self.endurance -= 1

    def walk(self):
        print(f"{self.name} гуляет.")

    def info(self):
        print(f"Имя война: {self.name}")
        print(f"Сила война: {self.power}")
        print(f"Выносливость война: {self.endurance}")
        print(f"Цвет волос война: {self.hair_color}")