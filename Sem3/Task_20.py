"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""
list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 8

rasn, numb = 0, 0
rasn = abs(k - list_1[0])
numb = list_1[0]
for i in range(1, len(list_1)):
#    print(list_1[i], rasn)
    if rasn > abs(k - list_1[i]):
        rasn = abs(k - list_1[i])
        numb = list_1[i]
print(numb)