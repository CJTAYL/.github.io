# Analysis of UK Basketball Coaches

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import statistics as stats
mpl.rcParams['figure.dpi'] = 200

# Winning Percentage
Cal = [.921, .763, .950, .636, .725, .974, .750, .842, .703, .811, .806, .360, .765]
Gillispie = [.581, .611]
Gil_seasons = ['1', '2']
Smith = [.897, .757, .697, .706, .688, .889, .844, .824, .629, .647]
Pitino = [.508, .786, .806, .882, .794, .848, .944, .875]

# Averages
avg_cal = stats.mean(Cal)
avg_gil = stats.mean(Gillispie)
avg_smi = stats.mean(Smith)
avg_pit = stats.mean(Pitino)

# SEC Tournament Championships
sec_tourney = {'Coach': ['Pitino', 'Smith', 'Gillispie', 'Calapari'], 
               'Championships' : [5, 5, 0, 6 ]}

sec_df = pd.DataFrame(sec_tourney)

# Total Wins 
total_wins = {'Coach': ['Pitino', 'Smith', 'Gillispie', 'Calapari'], 
               'Wins' : [269, 263, 40, 365]}

wins_df = pd.DataFrame(total_wins)

# Players Drafted 
players_drafted = {'Coach': ['Pitino', 'Smith', 'Gillispie', 'Calapari'], 
               'Players' : [5, 8, 2, 41]}

drafted_df = pd.DataFrame(players_drafted)

# Subplot of Pitino and Smith
from pyparsing.util import col

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(Pitino, '-o')
ax1.set_title("Pitino 89 - 96")
ax1.set_ylim(.3, 1)
ax1.set_xlabel("Season")
ax1.axhline(avg_pit, color="gray", linestyle="--")
ax2.plot(Smith, '-o')
ax2.set_title("Smith 97 - 06")
ax2.set_ylim(.3, 1)
ax2.set_xlabel("Season")
ax2.axhline(avg_smi, color="gray", linestyle="--")
plt.show()

# Subplot of Gillispie and Calipari
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(Gil_seasons, Gillispie, '-o')
ax1.set_title("Gillispie 07 - 08")
ax1.set_ylim(.3, 1)
ax1.set_xlabel("Season")
ax1.axhline(avg_gil, color="gray", linestyle="--")
ax2.plot(Cal, '-o')
ax2.set_ylim(.3, 1)
ax2.set_title("Calipari 09 - present")
ax2.set_xlabel("Season")
ax2.axhline(avg_cal, color="gray", linestyle="--")
plt.show()

# Total wins bar graph
plt.bar('Coach', 'Wins', data=wins_df, color = 'gray')
plt.title("Total Wins")
plt.ylabel("Wins")
plt.show()

# SEC tournament championships
plt.bar('Coach', 'Championships', data=sec_df, color = 'black')
plt.title("SEC Tournament")
plt.ylabel("Championships")
plt.show()

# Players drafted to the NBA bar graph
plt.bar('Coach', 'Players', data=drafted_df, color = 'orange')
plt.title("Drafted to NBA")
plt.ylabel("Players")
plt.show()
