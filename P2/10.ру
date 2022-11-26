# Реализуйте алгоритм перемешивания списка

import random


lenght = 20
list = [i for i in range (lenght)]

print(list, '<-- not mixed')

for i in range(len(list)):
    r = random.randint(i,lenght-1)
    m = list[i]
    list[i] = list[r]
    list[r] = m

print(list, '<-- mixed')

#Функция
random.shuffle(list)
print(list, '<-- shuffle')