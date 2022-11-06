"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

def mediane(array):
    '''
    Функция ищет медиану для массивов нечетной длины
    :param array:
    :return: 
    '''

    i = 1
    while i < len(array):
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    m = (len(array) - 1) // 2
    return array[m]


m = int(input('Введите число m для массива размером 2m + 1: '))
array = [randint(-100, 100) for i in range(2 * m + 1)]
print(array, f'Медиана равна {mediane(array[:])}', sep='\n')

# Замеры 10
array = [randint(-100, 100) for i in range(11)]
print(timeit('mediane(array[:])', globals=globals(), number=1000))
# Замеры 100
array = [randint(-100, 100) for i in range(101)]
print(timeit('mediane(array[:])', globals=globals(), number=1000))
# Замеры 1000
array = [randint(-100, 100) for i in range(1001)]
print(timeit('mediane(array[:])', globals=globals(), number=1000))

'''
Введите число m для массива размером 2m + 1: 10
[-71, -96, 46, 100, -8, 13, 86, 9, -12, 82, -60, 4, -32, 34, -87, -74, 91, 50, 94, -22, 2]
Медиана равна 4
0.021748634999999794
1.510360897
181.896992245
'''