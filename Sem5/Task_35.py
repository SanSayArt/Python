"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

def func_1(num):
    flag = True
    for el in range(2, num):
        if num % el == 0:
            flag = False
    return flag

n = 31
print(func_1(n))

def func_2(num, flag=True, i=2):
    if i < num:
        if num % i == 0:
            flag = False
        return func_2(num, flag, i + 1)
    return flag

print(func_2(n))

def func_3(num, flag=True, i=2):
    if i < int(num ** 0.5) + 1:
        if num % i == 0:
            flag = False
        return func_2(num, flag, i + 1)
    return flag

print(func_3(n))