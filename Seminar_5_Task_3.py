# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

A = [1, 2, 3, 4, 6, 7]
for i in range(1, len(A)):
    if A[i]-1 != A[i-1]:
        print(A[i-1]+1)