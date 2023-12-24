"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]

"""

list = [1, 2, 3, 4, 5]
k = 3
print(list)
for i in range(k):
    list.append(list[0])
    list.pop(0)
print(list)

list = [1, 2, 3, 4, 5]
print(list)
new_lst = list[k:] + list[:k]
print(new_lst)

print(list)
for i in range(k - 1):
    el = list.pop()
    list.insert(0, el)
print(list)