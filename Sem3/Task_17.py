"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6

"""

arr = [1, 1, 2, 0, -1, 3, 4, 4]

print(len(set(arr)))
print(set(arr))
# Традиционный итератор с функцией APPEND
lst = []
for el in arr:
    if el not in lst:
        lst.append(el)
print(len(lst))

# Списковое включение (lc)
# lst = [el for el in arr if el not in lst]
# print(len(lst))