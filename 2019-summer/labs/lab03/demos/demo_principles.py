class Produs:
    def __init__(self):
        self.__price = 5

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


bere = Produs()
print(bere.get_price())

bere.__price = 7
print(bere.get_price())

bere.set_price(7)
print(bere.get_price())

class Dog:
    def walk(self):
        print("I can walk")

class Fish:
    def walk(self):
        print("I can't walk")

def can_walk(animal):
    animal.walk()


rex = Dog()
nemo = Fish()

can_walk(rex)
can_walk(nemo)

class AudiA6:
    def __init__(self, color, price, hp):
        self.color = color
        self.price = price
        self.hp = hp


    def __str__(self):
        return "I am an A6"

    def __repr__(self):
        return "{self.__class__.__name__}('{self.color}', {self.price}, {self.hp})".format(self = self)

class AudiRS6(AudiA6):
    def __init__(self, color, price, hp):
        super().__init__(color, price, hp)

    def __str__(self):
        return "I am a RS6"

a6 = AudiA6("negru", 45000, 200)
rs6 = AudiRS6("negru", 65000, 400)

print(a6)
print(repr(a6))
print(rs6)

a6_v2 = eval(repr(a6))
print(a6_v2)
print(a6_v2.color)
print(str(a6))
print(rs6)
