'''
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
n = 4

def function1 (quantity):
    if quantity == 0:
        return ''
    number = input('Введите число: ')
    return function1(quantity-1) + number

print(function1(4))