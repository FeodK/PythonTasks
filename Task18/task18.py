'''
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
'''
N = int(input())
A = list(map(int, input().split()))
X = int(input())
min = abs(X - A[0])
index = 0
for i in range(1, N):
    count = abs(X - A[i])
    if count <= min:
        min = count
        index = i
print(A[index])