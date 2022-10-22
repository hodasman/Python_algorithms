
# Задание 3.
# Для этой задачи
# 1) придумайте 2-3 решения (обязательно с различной сложностью)
# 2) оцените сложность каждого выражения в этих решениях в нотации О-большое
# 3) оцените итоговую сложность каждого решения в нотации О-большое
# 4) сделайте вывод, какое решение эффективнее и почему
# Сама задача:
# Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
# Выведите результат.
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!


def top3(company: dict):
    '''
    Функция реализует поиск трех компаний с наибольшей годовой прибылью.
    :param company:
    :return:

    Сложность O(N^2)
    '''

    sorted_values = sorted(company.values(), reverse=True)  #O(NlogN)
    sorted_dict = {}                                        #O(1)

    for v in sorted_values:                 #O(N)
        for k in company.keys():            #O(N)
            if company[k] == v:             #O(1)
                sorted_dict[k] = company[k] #O(1)
                break
    sorted_list = list(sorted_dict.items()) #O(N)
    return sorted_list[0:3]                 #O(N)


def best3(company: dict):
    '''
    Функция реализует поиск трех компаний с наибольшей годовой прибылью.
    :param company:
    :return:

    Сложность O(NlogN)
    '''
    sorted_dict = {}                                            #O(1)
    sorted_keys = sorted(company, key=company.get, reverse=True)#O(NlogN)

    for w in sorted_keys:                       #O(N)
        sorted_dict[w] = company[w]             #O(1)
    sorted_list = list(sorted_dict.items())     #O(N)
    return sorted_list[0:3]                     #O(N)


forbes = {'Apple': 30000, 'Samsung': 50000, 'Huawei': 40000, 'Xiaomi': 45000}

print(top3(forbes))

print(best3(forbes))
