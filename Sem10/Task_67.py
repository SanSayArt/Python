"""
Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

pg = read_csv("penguins.csv")

pg.loc[pg['bill_length_mm'] < 35, 'height_group'] = "low"
pg.loc[(pg['bill_length_mm'] >= 35) & (pg['bill_length_mm'] < 42), 'height_group'] = "middle"
pg.loc[pg['bill_length_mm'] >= 42, 'height_group'] = "high"

pg.to_csv("penguins.csv")

