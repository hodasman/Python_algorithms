'''
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.

'''

def recursion_calc():

    oper = input('use operation (+, -, /, * or 0 if you want exit): ')

    if oper == '0':
        return 'good bye'
    try:
        if oper == '+':
            a = float(input('enter first digit: '))
            b = float(input('enter second digit: '))
            s = a + b
            print(s)
            return recursion_calc()

        if oper == '-':
            c = float(input('enter first digit: '))
            d = float(input('enter second digit: '))
            r = c - d
            print(r)
            return recursion_calc()

        if oper == '*':
            i = float(input('enter first digit: '))
            f = float(input('enter second digit: '))
            m = i * f
            print(m)
            return recursion_calc()

    except(ValueError) as e:
        print(f'you enter no digit {e}')
        return recursion_calc()

    try:
        if oper == '/':
            g = float(input('enter first digit: '))
            h = float(input('enter second digit: '))
            try:
                j = g/h
                print(j)
                return recursion_calc()
            except(ZeroDivisionError) as err:
                print(f'no zero division {err}')
                return recursion_calc()

    except(ValueError) as e:
        print(f'you enter no digit {e}')
        return recursion_calc()
    else:
        print('operation not found')
        return recursion_calc()



recursion_calc()