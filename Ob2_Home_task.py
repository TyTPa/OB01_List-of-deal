# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class Users():
# Этот класс должен инкапсулировать данные :
# ID, имя и уровень доступа ('user' для обычных сотрудников).
  def __init__(self, name, ID, level ='user'):
    self.name = name
    self.ID = ID
    self.level = level


  def info(self):
    print (f"{self.name} - имя")
    print (f"{self.ID} - персональный код")
    print (f"{self.level} - уровень допуска")


class Admin(Users):
  def __init__(self,name,ID, level="admin"):
      super().__init__(name, ID, level)  # Вызов конструктора родительского класса
      self.user = {}  # Словарь для хранения пользователей

  def add_user(self,name,ID,level = 'user'):
      new_user = Users(name, ID, level)  # Создаем нового пользователя
      self.user[new_user.ID] = new_user  # Сохраняем пользователя в словаре

  def remove_user(self, ID):
      if ID in self.user:
          self.user.pop(ID)  # Удаляем пользователя по ID
          print(f'Пользователь "{ID}" удален.')
      else:
          print(f'Пользователь "{ID}" не найден.')


admin1 = Admin('Петя', 1)
admin2 = Admin('Слава', 2)
print( admin1.info)

admin1.add_user('Анна', 3, 1)
admin1.add_user('Мелисса', 4, 1)

admin1.remove_user(3)  # Удаляем пользователя Анна
admin1.remove_user(5)  # Пытаемся удалить несуществующего пользователя
