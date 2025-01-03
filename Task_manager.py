# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода
# списка текущих (не выполненных) задач.
class Task():
 def __init__(self, name, deadline, status):
     self.name = name
     self.deadline = deadline
     self.status =status
def add():
     Task.name =input(f'введите описание задачи')
     Task.deadline = input(f'введите срок выполнения данной задачи')
     Task.status ='Не выполнено'
     print(f'Создана новая задача  {Task.name}')
def mark():
    Task.status = 'Выполнено'
def output():
    print(f'Статус {Task.name} задачи :{Task.status}')