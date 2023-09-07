'''

1. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Это неизвестное животное.")

class Fishes(Animal):

    def __init__(self, name, kind, age):
        super().__init__(name)
        self.kind = kind
        self.age = age
    
    def display_info(self):
        print(f"Это рыба по имени {self.name}. Вид - {self.kind}. Ей {self.age} лет.")

class Bird(Animal):
    def __init__(self, name, color, age):
        super().__init__(name)
        self.color = color
        self.age = age


    def display_info(self):
        print(f"Это птица вида {self.name}. Цвет оперения -  {self.color}. Возраст {self.age} год. ")

class Mammals(Animal):

    def __init__(self, name, kind, age, country):
        super().__init__(name)
        self.kind = kind
        self.age = age
        self.country = country

    def display_info(self):
        print(f"Это млекопитающее по имени {self.name}. Вид -   {self.kind}. Возраст {self.age} лет. Страна обитания {self.country} ")
    
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        if animal_type == "Fishes":
            return Fishes(name, kwargs.get("kind"), kwargs.get("age"))
        elif animal_type == "Bird":
            return Bird(name, kwargs.get("color"),kwargs.get("age"))
        elif animal_type == "Mammals":
            return Mammals(name, kwargs.get("kind"),kwargs.get("age"),kwargs.get ("country" ))
        else:
            return Animal(name)
        
fishes = AnimalFactory.create_animal("Fishes", "Дори", kind="клоун", age="5")
fishes.display_info()

bird = AnimalFactory.create_animal("Bird", "Чайка", color="белый", age="1")
bird.display_info()

mamml = AnimalFactory.create_animal("Mammals", "Лев", kind="кошачьи", age="6", country="Namibia")
mamml.display_info()

animal = AnimalFactory.create_animal("Animal", "Неизвестное животное")
animal.display_info()

