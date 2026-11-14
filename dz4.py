class Animal:
    def __init__(self, age, weight, legs, habitat):
        self.age = age
        self.weight = weight
        self.legs = legs
        self.habitat = habitat


    def describe(self):
        print("Its a/n", type(self).__name__)
        print("It is", self.age, "years old")
        print("It weighs", self.weight, "kg")
        print("It has", self.legs, "legs")
        print("It lives in", self.habitat)


class Dog(Animal):
    def __init__(self, age, weight):
        super().__init__(age, weight, 4, "home")


class Cat(Animal):
    def __init__(self, age, weight):
        super()__init__(age, weight, 4, "home, jungle, dessert")


class Bird(Animal):
    def __init__(self, age, weight):
        super().__init__(age, weight, 2, "sky, awamp")


class Fish(Animal):
    def __init__(self, age, weight):
        super().__init__(age, weight, 0, "water")


class Snake(Animal):
    def __init__(self, age, weight):
        super().__init__(age, weight, 0, "land, water")


animals = [Dog(8, 8), Cat(2, 4), Bird(1, 1), Fish(1, 2), Snake(4, 3)]

for animal in animals:
    animal.describe()
    print()
#Код не працює і я не знаю чому
