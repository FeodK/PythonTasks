'''
Решение в группах
В некоторой школе решили набрать три новых математических класса
 и оборудовать кабинеты для них новыми партами.
   За каждой партой может сидеть два учащихся.
     Известно количество учащихся в каждом из трех классов.
       Выведите наименьшее число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
'''
c1 = 20
c2 = 21
c3 = 22

# print((c1+c2+c3)//(-2)*(-1))

print((c1+1)//2 + c2//2 + (c2%2 != 0) + abs(-c3//2))