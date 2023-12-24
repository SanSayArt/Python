"""
Задача №21. Решение в группах
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]
# Традиционный итератор с функцией ADD() для множесьтва
my_set = set()
for el in lst_obj:
    for item in el.values():  # values - Значения, keys - ключи
        my_set.add(item)
print(my_set)

# множественное включение set comrehension
my_set = set(item for el in lst_obj for item in el.values())
print(my_set)