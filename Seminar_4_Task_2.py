# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

import random

N = int(input("Введите размер списка: "))
a = []

for i in range(N):
    new_element = random.randint(-N, N)
    a.append(new_element)
print(f'Ваш список: {a}')

print(f'Максимальное значение списка:{max(a)}, минимальное значение списка: {min(a)}')

# import re
# s = str(input())
# r = re.split(' ', s)
# t = map(int, r)
# k = map(int,r)
# print(min(t))
# print(max(k))