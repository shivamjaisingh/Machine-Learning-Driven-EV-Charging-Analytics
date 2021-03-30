import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from reading_data import data_meter_values, data_open_trans

df_open_transactions = data_open_trans()
df_meter_values = data_meter_values()

print(df_open_transactions.columns.values)
print(df_meter_values.columns.values)
print(df_open_transactions.describe(datetime_is_numeric=True, include="all").to_string())
print(df_open_transactions['TransactionStartTime'].head())
print(df_open_transactions['TransactionStopTime'].head())

print('Total Unique Start Cards out of ', (df_open_transactions['StartCard'].count()), ' : ',
      (df_open_transactions['StartCard'].nunique()))
print((df_open_transactions.groupby(['Day/Night'])['TotalEnergy'].sum()))
print((df_open_transactions.groupby(['Day/Night'])['MaxPower'].sum()))

print(df_open_transactions.groupby(['Start Integer Hour'])['TransactionId'].count())
df = pd.DataFrame(df_open_transactions.groupby(['Start Integer Hour'])['TransactionId'].count())
dd = df.plot()
dd.set_xticks(range(len(df)))
plt.show()


chargeTime = df_open_transactions['ChargeTime'] > 0
day = df_open_transactions['Day/Night'] == "Day"
night = df_open_transactions['Day/Night'] == "Night"

day_charge = df_open_transactions[chargeTime & day]
night_charge = df_open_transactions[chargeTime & night]
print(type(day_charge), day_charge.shape)
print(type(night_charge), night_charge.shape)

day_charge['ChargeTime'].hist(bins=50, alpha=0.5)
night_charge['ChargeTime'].hist(bins=50, alpha=0.4)
plt.show()

df1 = df_open_transactions['ChargeTime'].hist(bins=50)
dd1 = df1.plot()
plt.show()

sns.countplot(df_open_transactions['Day/Night'])
plt.show()

sns.countplot(df_open_transactions['Day of the Week'])
plt.show()
