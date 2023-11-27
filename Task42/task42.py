'''Узнать какая максимальная households в зоне минимального значения population'''

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
df_new=df.loc[df['population'] == df['population'].min(), ['households']]
max_households_in_min_population=df_new['households' ].max()
print(max_households_in_min_population)