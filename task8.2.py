"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""
class SemanticErr(Exception):
    pass

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root <= new_node:
                raise SemanticErr
            else:
                # если у узла нет левого потомка
                if self.left_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
        except SemanticErr:
            print(f'SemanticErr: Левый потомок должен быть меньше родителя: {self.root}')
        except TypeError as e:
            print(f'Неверное значение, введите число: {e}')


    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise SemanticErr
            else:
                # если у узла нет правого потомка
                if self.right_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                # если у узла есть правый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
        except SemanticErr:
            print(f'SemanticErr: Правый потомок должен быть больше или равен родителю: {self.root}')
        except TypeError as e:
            print(f'Неверное значение, введите число: {e}')

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
try:
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(7)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right(9)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().insert_right(11)
    print(r.get_right_child().get_right_child().get_root_val())
except Exception as e:
    print(f'global error: {e}')