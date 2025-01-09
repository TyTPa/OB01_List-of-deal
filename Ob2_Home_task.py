# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class Users():
# Этот класс должен инкапсулировать данные :
# ID, имя и уровень доступа ('user' для обычных сотрудников).
  def __init__(self, name, ID):
    self._name = name
    self._ID = ID
    self._level = 'user'


  def info(self):
    print (f"{self._name} - имя")
    print (f"{self._ID} - персональный код")
    print (f"{self._level} - уровень допуска")

  def get_ID(self):
       return self._ID
  def get_name(self):
       return self._name
  def get_level(self):
      return self._level

class Admin(Users):
  def __init__(self,name,ID):
      super().__init__(name, ID)  # Вызов конструктора родительского класса
      self._level ='admin'
      self.user = {}  # Словарь для хранения пользователей

  def add_user(self,name,ID):
      new_user = Users(name, ID)  # Создаем нового пользователя
      self.user[new_user._ID] = new_user  # Сохраняем пользователя в словаре

  def remove_user(self, ID):
      if ID in self.user:
          self.user.pop(ID)  # Удаляем пользователя по ID
          print(f'Пользователь "{ID}" удален.')
      else:
          print(f'Пользователь "{ID}" не найден.')


admin1 = Admin('Петя', 1)
admin2 = Admin('Слава', 2)
print( admin1.info)

admin1.add_user('Анна', 3)
admin1.add_user('Мелисса', 4)

admin1.remove_user(3)  # Удаляем пользователя Анна
admin1.remove_user(5)  # Пытаемся удалить несуществующего пользователя
