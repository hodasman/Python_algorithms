"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.basequeve = QueueClass()
        self.revisionqueve = QueueClass()
        self.solved = []

    def add_task(self, task):     # Добавление задачи в базовую очередь
        self.basequeve.to_queue(task)

    def to_solved(self):            # Перемещение решенной задачи в список решенных задач
        task = self.basequeve.from_queue()
        self.solved.append(task)

    def to_revision(self):          # Перемещение из базовой очереди на доработку
        task = self.basequeve.from_queue()
        self.revisionqueve.to_queue(task)

    def from_revision_to_solved(self):   # Перемещение из очереди на доработку в список решенных задач
        task = self.revisionqueve.from_queue()
        self.solved.append(task)

    def current_task(self):
        return self.basequeve.elems[len(self.basequeve.elems) - 1]

    def size(self):
        print(f" Задач в очереди: {self.basequeve.size()} задач на доработке: {self.revisionqueve.size()} выполнено задач {len(self.solved)}")




if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.add_task('task1')
    task_board.add_task('task2')
    task_board.add_task('task3')
    task_board.add_task('task4')
    task_board.size()
    print(task_board.current_task())
    task_board.to_solved()
    task_board.to_revision()
    task_board.to_revision()
    task_board.from_revision_to_solved()
    task_board.size()
