"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(3))


data['add_col'] = 1     # Добавляем столбец
data.set_index([data.index, 'whoAmI'], inplace=True)    # Создаем индекс по двум полям (ключ и "whoAmI") (добавляем уровни)
data = data.unstack(level=-1, fill_value = 0).astype(int)   # Преобразуем многоуровневую таблицу
data.columns = data.columns.droplevel()         # Удаляем уровень
data.columns.name = None    # Очищаем имя первого столбца
print(data.head(10))