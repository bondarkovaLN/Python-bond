# Задайте словарь из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from fractions import Fraction


input_num = int(input('Введите число: '))

list = []
sum = 0
for n in range(1,input_num+1):
    a = (1 + Fraction (1,n))**n
    sum += a #я не стал сумму делать отдельно, это будет просто пробегание по списку
    list.append (a)
print (sum)

print ('\nили')
list = [[],[]]
for n in range(1,input_num+1): #создание списка
    x = 1
    y = n
    x = x+1*y
    x = x**n
    y = y**n
    list[0].append(x)
    list[1].append(y)

for i in range(input_num): #сложение
    if i == 0:
        sum_x = list[0][i]
        sum_y = list[1][i]
    else:
        sum_x = sum_x * list[1][i] + sum_y * list[0][i]
        sum_y *= list[1][i]

print (sum_x,'/',sum_y)

print ('\nили')
sum = 0
for n in range(1,input_num+1):
    sum += (1+1/n)**n
print(sum)