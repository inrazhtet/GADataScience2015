# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:37:29 2015

@author: zarnihtet
"""

import pandas as pd
import matplotlib.pyplot as plt

flower_table = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

flower_cols = ['sepal_length', 'sepal_width','petal_length','petal_width','class']
flower_table.columns = flower_cols

flower_table.describe()