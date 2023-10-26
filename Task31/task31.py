'''
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
'''
n = int(input())
def fibonacci(index):
    if index <= 1:
        return 1
    return fibonacci(index-1) + fibonacci(index-2)
print(fibonacci(n))