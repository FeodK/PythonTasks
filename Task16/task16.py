'''
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
'''

N = int(input())
A = list(map(int, input().split()))
X = int(input())
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
print(count) 