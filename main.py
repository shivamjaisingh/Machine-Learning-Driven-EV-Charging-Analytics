import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime as dt
from datetime import datetime
from reading_data import data_open_trans

# from reading_data import data_meter_values
df_open_transactions = data_open_trans()
# df_meter_values = data_meter_values()

print(df_open_transactions.columns.values)
# print(df_meter_values.columns.values)

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


# date_year = pd.to_datetime(df_open_transactions['UTCTransactionStart'])
#
#
# def determine_peak(dto):
#     if dto.strftime("%B") in ["November", "December", "January", "February", "March", "April"]:
#         if (dto.strftime("%A") == "Saturday") or (dto.strftime("%A") == "Sunday") or (
#                 23 >= int(dto.strftime("%H")) >= 19) or (
#                 7 >= int(dto.strftime("%H")) >= 0):
#             return "OFF PEAK"
#         if 11 <= int(dto.strftime("%H")) <= 17:
#             return "MID PEAK"
#         else:
#             return "ON PEAK"
#     else:
#         if (dto.strftime("%A") == "Saturday") or (dto.strftime("%A") == "Sunday") or (
#                 23 >= int(dto.strftime("%H")) >= 19) or (
#                 7 >= int(dto.strftime("%H")) >= 0):
#             return "OFF PEAK"
#         if 11 <= int(dto.strftime("%H")) <= 17:
#             return "ON PEAK"
#         else:
#             return "MID PEAK"
#
#
# date_year['Peaks_Python'] = date_year.apply(lambda row: determine_peak(row))
#
# print(type(df_open_transactions))
# print(type(date_year))
# print(df_open_transactions)
# df_open_transactions['Peaks_Python'] = date_year.apply(lambda row: determine_peak(row))
# print(date_year['Peaks_Python'].head(10))

# df_open_transactions['Peaks_Python'] = date_year['Peaks_Python']
#
# print(df_open_transactions['Peaks_Python'])
#
# df_open_transactions.to_csv("dataset_new", sep=',', encoding='utf-8')

time_start = pd.to_datetime(df_open_transactions['UTCTransactionStart'])
time_stop = pd.to_datetime(df_open_transactions['UTCTransactionStop'])


def determine_peak_distribution(transaction_stop_time, transaction_start_time):
    on_hours = float(0)
    mid_hours = float(0)
    off_hours = float(0)

    total_hours_left = (transaction_stop_time - transaction_start_time)
    total_hours_left = total_hours_left.total_seconds() / 3600
    tt = total_hours_left
    start_hour = float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60
    print("Total Hours: ", total_hours_left, "Start Hour: ", start_hour)
    i = 0
    while total_hours_left > 0:
        print("Loop: ", i)
        i = i + 1
        if 0 <= start_hour < 7:  # only when time lies between 12 AM to 7 AM
            print("0-7")
            time_charged = total_hours_left if start_hour + total_hours_left < 7 else 7 - start_hour
            off_hours = off_hours + time_charged
            start_hour = start_hour if start_hour + total_hours_left < 7 else 7
            total_hours_left = total_hours_left - time_charged
            print("Total Hours Left: ", total_hours_left, "Off Hours: ", off_hours, "Time Charged: ", time_charged,
                  "Start Hour: ", start_hour)
        if 7 <= start_hour < 11:
            print("7-11")
            time_charged = total_hours_left if start_hour + total_hours_left < 11 else 11 - start_hour
            on_hours = on_hours + time_charged
            start_hour = start_hour if start_hour + total_hours_left < 11 else 11
            total_hours_left = total_hours_left - time_charged
            print("Total Hours Left: ", total_hours_left, "On Hours: ", on_hours, "Time Charged: ", time_charged,
                  "Start Hour: ", start_hour)

        if 11 <= start_hour < 17:
            print("11-17")
            time_charged = total_hours_left if start_hour + total_hours_left < 17 else 17 - start_hour
            mid_hours = mid_hours + time_charged
            start_hour = start_hour if start_hour + total_hours_left < 17 else 17
            total_hours_left = total_hours_left - time_charged
            print("Total Hours Left: ", total_hours_left, "Mid Hours: ", mid_hours, "Time Charged: ", time_charged,
                  "Start Hour: ", start_hour)

        if 17 <= start_hour < 19:
            print("17-19")
            time_charged = total_hours_left if start_hour + total_hours_left < 19 else 19 - start_hour
            on_hours = on_hours + time_charged
            start_hour = start_hour if start_hour + total_hours_left < 19 else 19
            total_hours_left = total_hours_left - time_charged
            print("Total Hours Left: ", total_hours_left, "On Hours: ", on_hours, "Time Charged: ", time_charged,
                  "Start Hour: ", start_hour)

        if 19 <= start_hour < 24:
            time_charged = total_hours_left if start_hour + total_hours_left < 24 else 24 - start_hour
            off_hours = off_hours + time_charged
            start_hour = start_hour if start_hour + total_hours_left < 24 else 0
            total_hours_left = total_hours_left - time_charged
            print("Total Hours Left: ", total_hours_left, "Off Hours: ", off_hours, "Time Charged: ", time_charged,
                  "Start Hour: ", start_hour)

    print("Total Hours: ", tt, "Off Hours: ", off_hours, "Mid Hours: ", mid_hours, "On Hours: ", on_hours)


determine_peak_distribution(time_stop[37], time_start[37])
