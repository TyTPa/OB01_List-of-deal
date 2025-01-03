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
 def mark(self):
    self.status = 'Выполнено'
 def output(self):
    if self.status=='Не выполнено':
        print(f' {self.name}  : Срок выполнения {self.deadline}')
 def info(self):
    print(f'Описание задачи - {self.name}')
    print(f'Статус задачи - {self.status}')
    print(f'Cрок выполнения- {self.deadline}')

class Task_Manager():
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input('Введите описание задачи: ')
        deadline = input('Введите срок выполнения данной задачи: ')
        status ='Не выполнено'
        task = Task(name, deadline, status)
        self.tasks.append(task)
#        print(f'Создана новая задача: {task.name}')

    def mark_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark()
            print(f'Задача "{self.tasks[task_index].name}" отмечена как выполненная.')
        else:
            print('Некорректный индекс задачи.')

    def output_current_tasks(self):
        print('Текущие (не выполненные) задачи:')
        for task in self.tasks:
            task.output()
task_manager=Task_Manager()
for i in range (2):
    task_manager.add_task()
# Указываем индекс задачи для отметки как выполненной
task_index_to_mark = int(input('Введите индекс задачи для отметки как выполненной (0 или 1): '))
task_manager.mark_task(task_index_to_mark)

# Выводим текущие задачи
task_manager.output_current_tasks()
