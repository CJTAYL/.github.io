import pandas as pd
import lxml
import matplotlib.pyplot as plt
from datetime import date

# Retrieving data from nerdwallet.com
nerd_wallet_table = pd.read_html('https://www.nerdwallet.com/article/mortgages/current-interest-rates')

# Converting data into a dataframe
df = nerd_wallet_table[1]

# Sub-setting the last two weeks of data
last_14 = df[0:14]

# Removing '%' from objects
fixed_30 = last_14['Average 30-year fixed APR'].str[:-1]
fixed_15 = last_14['Average 15-year fixed APR'].str[:-1]
arm_5 = last_14['Average 5 year ARM APR'].str[:-1]

# Converting objects to numerics
fixed_30n = pd.to_numeric(fixed_30, errors='coerce')
fixed_15n = pd.to_numeric(fixed_15, errors='coerce')
arm_5n = pd.to_numeric(arm_5, errors='coerce')

# Identifying the current date for plot
today = date.today()

# Plotting data
plt.plot(fixed_30n, '--o', label='Fixed 30-year')
plt.plot(fixed_15n, '--o', label='Fixed 15-year')
plt.plot(arm_5n, '-o', label='ARM 5-year')
plt.ylim(3.0, 7.5)
plt.suptitle('Mortgage Rates Last 14 Days')
plt.title(today)
plt.ylabel('Interest Rate')
plt.legend(loc="upper left")
plt.show()
