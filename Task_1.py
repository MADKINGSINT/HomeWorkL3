#     Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
ListSize = int(input('Введите размер списка:   '))
sp = []
def Fill_list(sp):
    for i in range (0, ListSize):
        temp = randint(0, ListSize)
        sp.append(temp)
Fill_list(sp)
print(sp)
answer = 0
for i in range (1, len(sp), 2):
    answer += sp[i]

print(answer)