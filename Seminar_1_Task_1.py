# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

a = int(input('Введите первое число а = '))
b = int(input('Введите второе число b = '))

if (b == a*a or a==b*b):
    print('yes')
else:
    print('no')
