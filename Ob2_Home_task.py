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
    self.user ={}

  def info(self):
    print (f"{self.name} - имя")
    print (f"{self.ID} - персональный код")
    print (f"{self.level} - уровень допуска")


class Admin(Users):
  def __init__(self,name,ID, level, status ="admin"):
    self.user ={}

  def add_user(self,name,ID,level):
      self.user.update({name:name, ID:ID,level: level})

  def remove_user(self, id):
      if id in self.user.ID:
          self.user.pop(id)
      else:
          print(f'пользователь "{id}" не найден.')

admin1 = Admin('Петя',1, 0, status ="admin")
admin2 = Admin('Слава',2, 0, status ="admin")

admin1.add_user('Анна',3,1)
admin1.add_user('Мелисса',3,1)
admin1.info()