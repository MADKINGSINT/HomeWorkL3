#     Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
ListSize = int(input('Введите размер списка:   '))
sp = []
def Fill_list(sp):
    for i in range (0, ListSize):
        temp = randint(0, ListSize)
        sp.append(temp)
Fill_list(sp)
print (sp)
sp2 = []
for i in range(len(sp)):
    while i < len(sp)/2 and ListSize > len(sp)/2:
        ListSize = ListSize - 1
        a = sp[i] * sp[ListSize]
        sp2.append(a)
        i += 1

print(sp2)