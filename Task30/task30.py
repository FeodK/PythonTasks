'''
Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: a,n = a,1  + (n-1) * d.
Каждое число вводится с новой строки.
'''
a, b, d = int(input()), int(input()), int(input())
mas = []
for i in range(a, a + (b * d), b):
    mas.append(i)
print(mas)