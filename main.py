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
print(df['IP'].describe())
print(df['ab'].describe())
print(df['p_era'].describe())
print(df['batting_avg'].describe())
print(df['home_run'].describe())
print(df['p_win'].describe())

wins = df[['p_win']]
print(wins)

plt.hist(wins, edgecolor = 'black', range = [0, 20])
plt.xlabel('Wins')
plt.ylabel('Frequency')
plt.title('Pitcher Win Frequency')
plt.show()

#multivariate analysis
