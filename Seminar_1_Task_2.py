# 2. Напишите программу, которая на вход принимает 5 чисел и
# находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите первое число а = '))
b = int(input('Введите второе число b = '))
c = int(input('Введите третье число c = '))
d = int(input('Введите четвертое число d = '))
e = int(input('Введите пятое число e = '))

max = a

# if (b>max):
#     max = b
# if (c>max):
#     max = c
# if (d>max):
#     max = d
# if (e>max):
#     max = e
# print (max)

numbers = [a, b, c, d, e]
for i in numbers:
    if (i > max):
        max = i
print(max)

