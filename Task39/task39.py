'''
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
'''
n = int(input('Введите количество элементов в первом массиве: '))
mas1 = [input() for _ in range(n)]
m = int(input('Введите количество элементов во втором массиве: '))
mas2 = [input() for _ in range(m)]
cnt = False
for el in mas1:
    if not el in mas2:
        print(el, end=' ')
            