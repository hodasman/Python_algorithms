"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    m = 0
    set_array = set(array)
    for num in set_array:
        count = array.count(num)
        if count > m:
            m = count
            el = num
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    max_count = 0
    m = 0
    s = set(array)
    for i in s:
        count = 0
        for k in array:
            if i == k:
                count +=1
        if max_count < count:
            max_count = count
            m = i
    return (m, max_count)

def counter():
    return Counter(array).most_common(1)

print(func_1())
print(func_2())
func_3()
func_4()
print(counter())
print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))
print(timeit('func_4()', globals=globals()))
print(timeit('counter()', globals=globals()))