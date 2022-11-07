"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

import statistics
from random import randint
from timeit import timeit

m = int(input('Введите число m для массива размером 2m + 1: '))
array = [randint(-100, 100) for i in range(2 * m + 1)]
print(array, f'Медиана равна {statistics.median(array[:])}', sep='\n')

# Замеры 10
array = [randint(-100, 100) for i in range(11)]
print(timeit('statistics.median(array[:])', globals=globals(), number=1000))
# Замеры 100
array = [randint(-100, 100) for i in range(101)]
print(timeit('statistics.median(array[:])', globals=globals(), number=1000))
# Замеры 1000
array = [randint(-100, 100) for i in range(1001)]
print(timeit('statistics.median(array[:])', globals=globals(), number=1000))

'''
Введите число m для массива размером 2m + 1: 2
[-90, -57, -95, -84, 72]
Медиана равна -84
0.0016424649999999819
0.0052517140000001294
0.1318417049999998

Просто коласальный отрыв метода median из модуля statistics. Хуже всего показала себя функция с Гномьей сортировкой.
'''