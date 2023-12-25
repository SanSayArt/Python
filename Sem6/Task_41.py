"""
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1
Вывод: Вывод:
0 2
"""

def sear(lst):
    count = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
    return count

lst_1 = [1, 6, 3, 6, 5, 7, 4]
print(sear(lst_1))

my_set = set()
for el in range(10):
    my_set.add(el)
my_set = {el for el in range(10)}

my_dict = {}
for el in range(10):
    my_dict[el] = str(el)
my_dict = {el: str(el) for el in range(10)}



print(my_set)
print(my_dict)