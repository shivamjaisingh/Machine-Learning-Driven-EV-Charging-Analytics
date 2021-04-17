import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime as dt
from reading_data import data_meter_values, data_open_trans

df_open_transactions = data_open_trans()
df_meter_values = data_meter_values()

print(df_open_transactions.columns.values)
print(df_meter_values.columns.values)

# print(df_open_transactions.describe(datetime_is_numeric=True, include="all").to_string())
# print(df_open_transactions['TransactionStartTime'].head())
# print(df_open_transactions['TransactionStopTime'].head())
#
# print('Total Unique Start Cards out of ', (df_open_transactions['StartCard'].count()), ' : ',
#       (df_open_transactions['StartCard'].nunique()))
# print((df_open_transactions.groupby(['Day/Night'])['TotalEnergy'].sum()))
# print((df_open_transactions.groupby(['Day/Night'])['MaxPower'].sum()))
# # first graph
# print(df_open_transactions.groupby(['Start Integer Hour'])['TransactionId'].count())
# df = pd.DataFrame(df_open_transactions.groupby(['Start Integer Hour'])['TransactionId'].count())
# dd = df.plot()
# dd.set_xticks(range(len(df)))
# plt.show()
# # first graph
#
# chargeTime = df_open_transactions['ChargeTime'] > 0
# day = df_open_transactions['Day/Night'] == "Day"
# night = df_open_transactions['Day/Night'] == "Night"
#
# day_charge = df_open_transactions[chargeTime & day]
# night_charge = df_open_transactions[chargeTime & night]
# print(type(day_charge), day_charge.shape)
# print(type(night_charge), night_charge.shape)
#
# day_charge['ChargeTime'].hist(bins=50, alpha=0.5)
# night_charge['ChargeTime'].hist(bins=50, alpha=0.4)
# plt.show()
#
# df1 = df_open_transactions['ChargeTime'].hist(bins=50)
# dd1 = df1.plot()
# plt.show()
#
# sns.countplot(df_open_transactions['Day/Night'])
# plt.show()
#
# sns.countplot(df_open_transactions['Day of the Week'])
# plt.show()
#
# x1 = df_open_transactions['TransactionId']
# y1 = df_open_transactions['ConnectedTime']
# plt.scatter(x1, y1, s=2,  label="Connected Time")
#
# x2 = df_open_transactions['TransactionId']
# y2 = df_open_transactions['ChargeTime']
#
# plt.scatter(x2, y2, s=2, label="Charge Time")
#
# plt.xlabel("Transaction IDs")
# plt.title("Connected Time vs Charge Time")
# plt.legend()
# plt.xticks(x2, "")
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=True)
# plt.show()
#
#
# plt.clf()
# df2 = df_meter_values['Collectedvalue'].hist(bins=100, )
# df2.plot()
# plt.ylabel("Collected Value")
# plt.show()


# on = df_open_transactions['String_P'].str.count("ON PEAK")
#
# mid = df_open_transactions['String_P'].str.count("MID PEAK")
#
# off = df_open_transactions['String_P'].str.count("OFF PEAK")


# print(on, mid, off)
# peaks = [on, mid, off]
# plt.pie(peaks)
# plt.show()


date_year = pd.to_datetime(df_open_transactions['UTCTransactionStart'])

def determine_peak(dto):
    if dto.strftime("%B") in ["November", "December", "January", "February", "March", "April"]:
        if (dto.strftime("%A") == "Saturday") or (dto.strftime("%A") == "Sunday") or (
                23 >= int(dto.strftime("%H")) >= 19) or (
                7 >= int(dto.strftime("%H")) >= 0):
            return "OFF PEAK"
        if 11 <= int(dto.strftime("%H")) <= 17:
            return "MID PEAK"
        else:
            return "ON PEAK"
    else:
        if (dto.strftime("%A") == "Saturday") or (dto.strftime("%A") == "Sunday") or (
                23 >= int(dto.strftime("%H")) >= 19) or (
                7 >= int(dto.strftime("%H")) >= 0):
            return "OFF PEAK"
        if 11 <= int(dto.strftime("%H")) <= 17:
            return "ON PEAK"
        else:
            return "MID PEAK"


print(date_year[4].strftime("%A-%H"))

date_year['Peaks_Python'] = date_year.apply(lambda row: determine_peak(row))
print(date_year['Peaks_Python'].head(10))


