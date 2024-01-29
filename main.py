import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

plt.style.use('ggplot')
pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/dtgiv/Downloads/stats.csv')
print(df.shape)

print(df.head())

print(df.columns)

#drop 'unnamed: 26' and 'year' columns
df = df[['last_name, first_name', 'player_id', 'player_age',
       'p_formatted_ip', 'ab', 'hit', 'single', 'double', 'triple', 'home_run',
       'k_percent', 'bb_percent', 'batting_avg', 'slg_percent',
       'on_base_percent', 'on_base_plus_slg', 'p_save', 'p_win', 'p_loss',
       'p_shutout', 'p_era', 'p_total_stolen_base', 'p_rbi', 'p_quality_start',
       'p_called_strike']].copy()

print(df.columns)

print(df.dtypes)

#rename columns
df.rename(columns = {'last_name, first_name':'name', 'player_age':'age',
                     'p_formatted_ip':'IP', 'hit':'hits'}, inplace = True)

print(df.columns)

print(df.head())

print(df.duplicated())

#feature understanding
#univariate analysis
print(df['IP'].min())
print(df['IP'].mean())
print(df['ab'].min())
print(df['ab'].mean())
print(df['p_era'].max())
print(df['p_era'].min())
print(df['p_era'].mean())
print(df['batting_avg'].max())
print(df['batting_avg'].min())
print(df['home_run'].max())

'''
ax = df['p_win'].value_counts() \
    .plot(kind = 'barh', title = '2023 Win Counts')
ax.set_xlabel('Number of Pitchers')
ax.set_ylabel('Number of Wins')
plt.show()
'''
