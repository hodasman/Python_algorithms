"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


def haffman_tree(s: str):
    count = Counter(s)
    sorted_el = deque(sorted(count.items(), key=lambda item: item[1]))

    while len(sorted_el) > 1:

        weight = sorted_el[0][1] + sorted_el[1][1]
        union = {0: sorted_el.popleft()[0], 1: sorted_el.popleft()[0]}

        for i, item in enumerate(sorted_el):
            if weight > item[1]:
                continue
            else:
                sorted_el.insert(i, (union, weight))
                break
        else:
            sorted_el.append((union, weight))

    return sorted_el[0][0]


code_table = dict()


def haffman_code(tree, path=''):

    if not isinstance(tree, dict):
        code_table[tree] = path

    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "beep boop beer!"

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
