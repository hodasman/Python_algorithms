"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


def find_min(lst: list):
    '''
    Функция ищет минимальное значение в списке
    :param lst:
    :return:

    Сложность O(N^2)
    '''
    lenght = len(lst)
    for i in range(lenght):
        for j in range(0, lenght-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j + 1] = temp
    return lst[0]


def find_min2(lst: list):
    '''
    Функция ищет минимальное значение в списке
    :param lst: 
    :return:

    Сложность #O(N)
    '''
    min_numb = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_numb:
            min_numb = lst[i]
    return min_numb


lst = [8, 4, 6, 5, 4, 9, 12]

print(find_min(lst))

print(find_min2(lst))
