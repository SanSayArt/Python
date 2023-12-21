n = 123

# Введите ваше решение ниже
j = 0
for i in range(3):
    j += n % 10
    n = n // 10
 
res = j
print(res)