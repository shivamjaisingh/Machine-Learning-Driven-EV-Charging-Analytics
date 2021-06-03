import pandas as pd
from reading_data import data_open_trans
import matplotlib.pyplot as plt

pd.options.display.width = None

df_open_transactions = data_open_trans()
df_open_transactions = df_open_transactions[df_open_transactions['ConnectedTime'] <= 24]

time_start = pd.to_datetime(df_open_transactions['UTCTransactionStart'])
time_stop = pd.to_datetime(df_open_transactions['UTCTransactionStop'])


def determine_peak_distribution(transaction_stop_time, transaction_start_time):
    # print(transaction_start_time.strftime("%A") in ["Saturday", "Sunday"])
    if transaction_start_time.strftime("%B") in ["November", "December", "January", "February", "March", "April"]:
        on_hours = float(0)
        mid_hours = float(0)
        off_hours = float(0)
        super_off_hours = float(0)
        total_hours_left = (transaction_stop_time - transaction_start_time)
        total_hours_left = total_hours_left.total_seconds() / 3600
        t_hours = total_hours_left
        # if transaction_start_time.strftime("%A") and transaction_stop_time.strftime("%A") in ["Saturday",
        # "Sunday"]: off_hours = total_hours_left mid_hours = 0 on_hours = 0 print("Total Hours:",
        # total_hours_left, "Off Hours:", off_hours, "Mid Hours:", mid_hours, "On Hours:", on_hours) return
        # tt = total_hours_left
        start_hour = float(transaction_start_time.strftime("%H")) + float(
            transaction_start_time.strftime("%M")) / 60
        # print("Total Hours: ", total_hours_left, "Start Hour: ", start_hour)
        i = 0
        while total_hours_left > 0:
            # print("Loop: ", i)
            i = i + 1
            if 0 <= start_hour < 8:  # only when time lies between 12 AM to 7 AM
                # print("0-7")
                time_charged = total_hours_left if start_hour + total_hours_left < 8 else 8 - start_hour
                off_hours = off_hours + time_charged
                start_hour = start_hour if start_hour + total_hours_left < 8 else 8
                total_hours_left = total_hours_left - time_charged
                # print("Total Hours Left: ", total_hours_left, "Off Hours: ", off_hours, "Time Charged: ",
                #     time_charged,
                #      "Start Hour: ", start_hour)

            if 8 <= start_hour < 16:
                # print("7-11")
                time_charged = total_hours_left if start_hour + total_hours_left < 16 else 16 - start_hour
                super_off_hours = super_off_hours + time_charged
                start_hour = start_hour if start_hour + total_hours_left < 16 else 16
                total_hours_left = total_hours_left - time_charged
                # print("Total Hours Left: ", total_hours_left, "On Hours: ", on_hours, "Time Charged: ",
                #     time_charged,
                #      "Start Hour: ", start_hour)

            if 16 <= start_hour < 21:
                # print("11-17")
                time_charged = total_hours_left if start_hour + total_hours_left < 21 else 21 - start_hour
                mid_hours = mid_hours + time_charged
                start_hour = start_hour if start_hour + total_hours_left < 21 else 21
                total_hours_left = total_hours_left - time_charged
                # print("Total Hours Left: ", total_hours_left, "Mid Hours: ", mid_hours, "Time Charged: ",
                #      time_charged,
                #      "Start Hour: ", start_hour)

            if 21 <= start_hour < 24:
                time_charged = total_hours_left if start_hour + total_hours_left < 24 else 24 - start_hour
                off_hours = off_hours + time_charged
                start_hour = start_hour if start_hour + total_hours_left < 24 else 0
                total_hours_left = total_hours_left - time_charged
                # print("Total Hours Left: ", total_hours_left, "Off Hours: ", off_hours, "Time Charged: ",
                #      time_charged,
                #      "Start Hour: ", start_hour)

        return str(round((on_hours/t_hours)*100, 3)) + "%, " + str(round((off_hours/t_hours)*100, 3)) + "%, " + str(round((mid_hours/t_hours)*100, 3)) + "%, " + str(
            round((super_off_hours/t_hours)*100, 3))+"%"

    else:
        if (transaction_start_time.strftime("%A") in ["Saturday", "Sunday"]) and (
                transaction_stop_time.strftime("%A") in
                ["Saturday", "Sunday"]):
            on_hours = float(0)
            mid_hours = float(0)
            off_hours = float(0)
            super_off_hours = float(0)

            total_hours_left = (transaction_stop_time - transaction_start_time)
            total_hours_left = total_hours_left.total_seconds() / 3600
            t_hours = total_hours_left
            # if transaction_start_time.strftime("%A") and transaction_stop_time.strftime("%A") in ["Saturday",
            # "Sunday"]: off_hours = total_hours_left mid_hours = 0 on_hours = 0 print("Total Hours:",
            # total_hours_left, "Off Hours:", off_hours, "Mid Hours:", mid_hours, "On Hours:", on_hours) return
            # tt = total_hours_left
            start_hour = float(transaction_start_time.strftime("%H")) + float(
                transaction_start_time.strftime("%M")) / 60
            # print("Total Hours:", total_hours_left, "Start Hour:", start_hour)
            i = 0
            while total_hours_left > 0:
                # print("Loop: ", i)
                i = i + 1
                if 0 <= start_hour < 8:  # only when time lies between 12 AM to 7 AM
                    # print("0-7")
                    time_charged = total_hours_left if start_hour + total_hours_left < 8 else 8 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 8 else 8
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Off Hours:", off_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)
                if 8 <= start_hour < 16:
                    # print("7-11")
                    time_charged = total_hours_left if start_hour + total_hours_left < 16 else 16 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 16 else 16
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Mid Hours:", mid_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

                if 16 <= start_hour < 21:
                    # print("11-17")
                    time_charged = total_hours_left if start_hour + total_hours_left < 21 else 21 - start_hour
                    mid_hours = mid_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 21 else 21
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "On Hours:", on_hours, "Time Charged:", time_charged,
                    #     "Start Hour:", start_hour)

                if 21 <= start_hour < 24:
                    time_charged = total_hours_left if start_hour + total_hours_left < 24 else 24 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 24 else 0
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Off Hours:", off_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

            return str(round((on_hours/t_hours)*100, 3)) + "%, " + str(round((off_hours/t_hours)*100, 3)) + "%, " + str(
                round((mid_hours/t_hours)*100, 3)) + "%, " + str(round((super_off_hours/t_hours)*100, 3))+"%"
        else:
            on_hours = float(0)
            mid_hours = float(0)
            off_hours = float(0)
            super_off_hours = float(0)

            total_hours_left = (transaction_stop_time - transaction_start_time)
            total_hours_left = total_hours_left.total_seconds() / 3600
            t_hours = total_hours_left
            # if transaction_start_time.strftime("%A") and transaction_stop_time.strftime("%A") in ["Saturday",
            # "Sunday"]: off_hours = total_hours_left mid_hours = 0 on_hours = 0 print("Total Hours:",
            # total_hours_left, "Off Hours:", off_hours, "Mid Hours:", mid_hours, "On Hours:", on_hours) return
            # tt = total_hours_left
            start_hour = float(transaction_start_time.strftime("%H")) + float(
                transaction_start_time.strftime("%M")) / 60
            # print("Total Hours:", total_hours_left, "Start Hour:", start_hour)
            i = 0
            while total_hours_left > 0:
                # print("Loop: ", i)
                i = i + 1
                if 0 <= start_hour < 8:  # only when time lies between 12 AM to 7 AM
                    # print("0-7")
                    time_charged = total_hours_left if start_hour + total_hours_left < 8 else 8 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 8 else 8
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Off Hours:", off_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)
                if 8 <= start_hour < 16:
                    # print("7-11")
                    time_charged = total_hours_left if start_hour + total_hours_left < 16 else 16 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 16 else 16
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Mid Hours:", mid_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

                if 16 <= start_hour < 21:
                    # print("11-17")
                    time_charged = total_hours_left if start_hour + total_hours_left < 21 else 21 - start_hour
                    on_hours = on_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 21 else 21
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "On Hours:", on_hours, "Time Charged:", time_charged,
                    #     "Start Hour:", start_hour)

                if 21 <= start_hour < 24:
                    time_charged = total_hours_left if start_hour + total_hours_left < 24 else 24 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 24 else 0
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Off Hours:", off_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

            return str(round((on_hours/t_hours)*100, 3)) + "%, " + str(round((off_hours/t_hours)*100, 3)) + "%, " + str(
                round((mid_hours/t_hours)*100, 3)) + "%, " + str(round((super_off_hours/t_hours)*100, 3))+"%"


print(determine_peak_distribution(time_stop[25], time_start[25]))

df_open_transactions['On-Off-Mid-SuperOff-Peak-Distribution'] = \
    df_open_transactions.apply(lambda x: determine_peak_distribution(x['UTCTransactionStop'], x['UTCTransactionStart']),
                               axis=1)

df_1 = df_open_transactions[['ConnectedTime', 'On-Off-Mid-SuperOff-Peak-Distribution']].head(20)

plt.axis('off')
plt.axis('tight')
plt.table(cellText=df_1.values, colLabels=df_1.columns,
          cellLoc='center', colColours=['yellow', 'pink'],
          loc='center')
plt.title("Peak distribution", y=1)
plt.axis('tight')
plt.savefig("Peak distribution of connected time-TOU-7", dpi=600)
plt.show()
plt.close()
