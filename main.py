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

plt.hist(wins, edgecolor = 'black', bins = 20)
plt.xlabel('Wins')
plt.ylabel('Frequency')
plt.title('Pitcher Win Frequency')
plt.show()

quality_starts = df[['p_quality_start']]
print(quality_starts)

plt.hist(quality_starts, edgecolor = 'black', bins = 25)
plt.xlabel('Number of Quality Starts')
plt.ylabel('Frequency')
plt.title('Pitcher Quality Start Frequency')
plt.show()

era = df[['p_era']]
print(era)

plt.hist(era, edgecolor = 'black', bins = 28)
plt.xlabel('ERA')
plt.ylabel('Frequency')
plt.title('Pitcher ERA Frequency')
plt.show()

#multivariate analysis
df[['age', 'batting_avg']].plot(kind = 'scatter', x = 'age', y = 'batting_avg')
plt.title('Opposition Batting Average by Pitcher Age',)
plt.xlabel('Pitcher Age')
plt.ylabel('Batting Average')
plt.show()

df[['age', 'IP']].plot(kind = 'scatter', x = 'age', y = 'IP')
plt.title('Innings Pitched by Pitcher Age',)
plt.xlabel('Pitcher Age')
plt.ylabel('Innings Pitched')
plt.show()

df[['age', 'p_quality_start']].plot(kind = 'scatter', x = 'age', y = 'p_quality_start')
plt.title('Quality Starts by Pitcher Age',)
plt.xlabel('Pitcher Age')
plt.ylabel('Quality Starts')
plt.show()

df[['p_loss', 'p_total_stolen_base']].plot(kind = 'scatter', x = 'p_loss', y = 'p_total_stolen_base')
plt.title('Stolen Bases Allowed by Total Losses',)
plt.xlabel('Number of Losses')
plt.ylabel('Stolen Bases Allowed')
plt.show()

df[['p_win', 'p_total_stolen_base']].plot(kind = 'scatter', x = 'p_win', y = 'p_total_stolen_base')
plt.title('Stolen Bases Allowed by Total Wins',)
plt.xlabel('Number of Wins')
plt.ylabel('Stolen Bases Allowed')
plt.show()

df[['k_percent', 'bb_percent']].plot(kind = 'scatter', x = 'k_percent', y = 'bb_percent')
plt.title('Walk Percentage by Strike Percentage',)
plt.xlabel('Strike Percentage')
plt.ylabel('Walk Percentage')
plt.show()