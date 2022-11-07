"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def mediana_no_sort(array):
    m = 1
    l = (len(array) - 1) // 2
    while m <= l:
        array.remove(max(array))
        m += 1
    return max(array)


m = int(input('Введите число m для массива размером 2m + 1: '))
array = [randint(-100, 100) for i in range(2 * m + 1)]
print(array, f'Медиана равна {mediana_no_sort(array[:])}', sep='\n')

# Замеры 10
array = [randint(-100, 100) for i in range(11)]
print(timeit('mediana_no_sort(array[:])', globals=globals(), number=1000))
# Замеры 100
array = [randint(-100, 100) for i in range(101)]
print(timeit('mediana_no_sort(array[:])', globals=globals(), number=1000))
# Замеры 1000
array = [randint(-100, 100) for i in range(1001)]
print(timeit('mediana_no_sort(array[:])', globals=globals(), number=1000))

'''
Введите число m для массива размером 2m + 1: 2
[-10, 45, 4, 72, -33]
Медиана равна 4
0.006202414999999961
0.1636987729999999
13.235409522000001
'''