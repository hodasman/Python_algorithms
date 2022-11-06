"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit


def reverse_bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def reverse_bubble_sort2(lst):
    n = 1
    swapped = True
    while n < len(lst) and swapped:
        swapped = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        n += 1
    return lst

lst_obj = [randint(-100, 100) for _ in range(100)]
print(lst_obj, reverse_bubble_sort(lst_obj[:]), sep='\n')
print('Не оптимизированная функция сортировки: ', timeit('reverse_bubble_sort(lst_obj[:])', globals=globals(), number=1000), sep=' ')
print(lst_obj, reverse_bubble_sort2(lst_obj[:]), sep='\n')
print('Оптимизированная функция сортировки: ', timeit('reverse_bubble_sort2(lst_obj[:])', globals=globals(), number=1000), sep=' ')

'''Оптимизированная функция не дает выйгрыш по времени в небольших массивах и очень редко в больших массивах (чаще оптимизированная функция работает дольше)
поэтому использование ее не целесообразно'''