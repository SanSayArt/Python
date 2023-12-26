"""
Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
"""

from pandas import read_csv
from seaborn import histplot
from matplotlib.pylab import show

pg = read_csv("penguins.csv")

histplot(pg, x="flipper_length_mm", hue="height_group")

show()