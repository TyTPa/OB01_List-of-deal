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

# Создаем класс без наследования и прописываем как функцию инициализации с характеристиками
class Zoo:
    def __init__(self):
       self.Animals =[] # Список для хранения животных
       self.Employees = []  # Список для хранения сотрудников
    def add_animal(self,name):
       self.Animals.append (name) # добавляем новое животное
    def add_employee(self,name):
       self.Employees.append (name)  # Добавляем нового сотрудника
    def info(self):
        print("Животные в зоопарке:")
        for animal in self.Animals:
            print(f"- {animal.name}, возраст: {animal.age}")
        print("Сотрудники в зоопарке:")
        for employee in self.Employees:
            print(f"- {employee.name}")

    def write_file(self):
        with open("zoo_data.txt", "w", encoding="utf-8") as file:
            file.write("Животные в зоопарке:/n")
            for animal in self.Animals:
                file.write(f"- {animal.name}, возраст: {animal.age}")
            file.write("Сотрудники в зоопарке:")
            for employee in self.Employees:
                employee_class = type(employee).__name__  # Получаем имя класса сотрудника
                print(f"- {employee.name}, класс: {employee_class}")

# Сотрудники ZOO
class Employee():
    def __init__(self, name):
        self.name = name
class ZooKeeper (Employee):
     def __init__(self, name):
         super().__init__(name)  # Вызов конструктора родительского класса
     def feed_animal(self,animal):
         print(f"{self.name} кормит {animal.name}")
class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name)  # Вызов конструктора родительского класса
    def heel_animal(self,animal):
        print(f"{self.name} лечит {animal.name}")

ZOO_animals = [Bird('Parrot',3), Mammal('Tiger',20), Reptile('Varan',5)]
for animal in ZOO_animals:
    animal.make_sound()
    animal.eat()


zoo= Zoo()
# Добавляем животных
zoo.add_animal(Bird('Попугай', 3))
zoo.add_animal(Mammal('Тигр', 20))
zoo.add_animal(Reptile('Варан', 5))

# Добавляем сотрудников
zoo.add_employee(ZooKeeper("Саша"))
zoo.add_employee(Veterinarian ("Петя"))

# Вызываем звуки животных
for animal in zoo.Animals:
    animal.make_sound()
    animal.eat()

# Выводим информацию о зоопарке
zoo.info()
# Записываем данные в файл
zoo.write_file()
# Пример использования сотрудников
zoo.Employees[0].feed_animal(zoo.Animals[0])  # Саша кормит Попугая

