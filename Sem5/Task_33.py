"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

def max_to_min(lst, count, x):
    if count < 0:
        return lst
    count -= 1
    if lst[count] == x:
        lst[count] = min(lst)
    return max_to_min(lst, count, x)


list_1 = [1, 3, 3, 3, 4]
cnt = 5

print(max_to_min(list_1, cnt, max(list_1)))