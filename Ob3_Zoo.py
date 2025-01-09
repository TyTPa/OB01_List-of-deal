# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
class Animal():
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        print (self.name,f'кушает')

class Bird(Animal):
   def __init__(self, name, age):
        super().__init__(name, age)  # Вызов конструктора родительского класса

   def make_sound(self):
        print(self.name, 'кричит Ар-ар-ар')



class Mammal(Animal):
    def make_sound(self):
        print(self.name, 'кричит ррррррр')

class Reptile(Animal):
    def make_sound(self):
        print(self.name, 'кричит шшшшш')

ZOO_animals = [Bird('Parrot',3), Mammal('Tiger',20), Reptile('Varan',5)]
for animal in ZOO_animals:
    animal.make_sound()
    animal.eat()