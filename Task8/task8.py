'''
Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).

3 2 4 -> yes
3 2 1 -> no

'''

m, n, k = int(input()), int(input()), int(input())
result = ['NO', 'YES']
print(result[k % m == 0 or k % n == 0])