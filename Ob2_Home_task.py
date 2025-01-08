# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class Users():
# Этот класс должен инкапсулировать данные :
# ID, имя и уровень доступа ('user' для обычных сотрудников).
  def __init__(self, name, ID, level):
    self.name = name
    self.ID = ID
    self.level = level


  def info(self):
    print (f"{self.name} - имя")
    print (f"{self.ID} - персональный код")
    print (f"{self.level} - уровень допуска")


class Admin(Users):
  def __init__(self,name,ID, level, status ="admin"):
      super().__init__(name, ID, level)  # Вызов конструктора родительского класса
      self.users = {}  # Словарь для хранения пользователей

  def add_user(self,name,ID,level):
      new_user = User(name, ID, level)  # Создаем нового пользователя
      self.users[new_user.ID] = new_user  # Сохраняем пользователя в словаре

  def remove_user(self, id):
      if ID in self.users:
          self.users.pop(ID)  # Удаляем пользователя по ID
          print(f'Пользователь "{ID}" удален.')
      else:
          print(f'Пользователь "{ID}" не найден.')


admin1 = Admin('Петя',1, 0, status ="admin")
admin2 = Admin('Слава',2, 0, status ="admin")

admin1.add_user('Анна',3,1)
admin1.add_user('Мелисса',3,1)
admin1.info()