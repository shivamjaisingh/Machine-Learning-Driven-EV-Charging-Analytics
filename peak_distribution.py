import pandas as pd
from reading_data import data_open_trans

df_open_transactions = data_open_trans()

time_start = pd.to_datetime(df_open_transactions['UTCTransactionStart'])
time_stop = pd.to_datetime(df_open_transactions['UTCTransactionStop'])


def determine_peak_distribution(transaction_stop_time, transaction_start_time):
    # print(transaction_start_time.strftime("%A") in ["Saturday", "Sunday"])
    if (transaction_start_time.strftime("%A") in ["Saturday", "Sunday"]) and (transaction_stop_time.strftime("%A") in
                                                                              ["Saturday", "Sunday"]):
        total_hours_left = (transaction_stop_time - transaction_start_time)
        total_hours_left = total_hours_left.total_seconds() / 3600
        return "0.0, " + str(round(total_hours_left, 3)) + ", 0.0"
    else:

        if transaction_start_time.strftime("%B") in ["November", "December", "January", "February", "March", "April"]:
            on_hours = float(0)
            mid_hours = float(0)
            off_hours = float(0)
            total_hours_left = (transaction_stop_time - transaction_start_time)
            total_hours_left = total_hours_left.total_seconds() / 3600
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
                if 0 <= start_hour < 7:  # only when time lies between 12 AM to 7 AM
                    # print("0-7")
                    time_charged = total_hours_left if start_hour + total_hours_left < 7 else 7 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 7 else 7
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left: ", total_hours_left, "Off Hours: ", off_hours, "Time Charged: ",
                    #     time_charged,
                    #      "Start Hour: ", start_hour)

                if 7 <= start_hour < 11:
                    # print("7-11")
                    time_charged = total_hours_left if start_hour + total_hours_left < 11 else 11 - start_hour
                    on_hours = on_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 11 else 11
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left: ", total_hours_left, "On Hours: ", on_hours, "Time Charged: ",
                    #     time_charged,
                    #      "Start Hour: ", start_hour)

                if 11 <= start_hour < 17:
                    # print("11-17")
                    time_charged = total_hours_left if start_hour + total_hours_left < 17 else 17 - start_hour
                    mid_hours = mid_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 17 else 17
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left: ", total_hours_left, "Mid Hours: ", mid_hours, "Time Charged: ",
                    #      time_charged,
                    #      "Start Hour: ", start_hour)

                if 17 <= start_hour < 19:
                    # print("17-19")
                    time_charged = total_hours_left if start_hour + total_hours_left < 19 else 19 - start_hour
                    on_hours = on_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 19 else 19
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left: ", total_hours_left, "On Hours: ", on_hours, "Time Charged: ",
                    #      time_charged,
                    #      "Start Hour: ", start_hour)

                if 19 <= start_hour < 24:
                    time_charged = total_hours_left if start_hour + total_hours_left < 24 else 24 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 24 else 0
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left: ", total_hours_left, "Off Hours: ", off_hours, "Time Charged: ",
                    #      time_charged,
                    #      "Start Hour: ", start_hour)

            return str(round(on_hours, 3)) + ", " + str(round(off_hours, 3)) + ", " + str(round(mid_hours, 3))

        else:
            on_hours = float(0)
            mid_hours = float(0)
            off_hours = float(0)

            total_hours_left = (transaction_stop_time - transaction_start_time)
            total_hours_left = total_hours_left.total_seconds() / 3600
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
                if 0 <= start_hour < 7:  # only when time lies between 12 AM to 7 AM
                    # print("0-7")
                    time_charged = total_hours_left if start_hour + total_hours_left < 7 else 7 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 7 else 7
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Off Hours:", off_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)
                if 7 <= start_hour < 11:
                    # print("7-11")
                    time_charged = total_hours_left if start_hour + total_hours_left < 11 else 11 - start_hour
                    mid_hours = mid_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 11 else 11
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Mid Hours:", mid_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

                if 11 <= start_hour < 17:
                    # print("11-17")
                    time_charged = total_hours_left if start_hour + total_hours_left < 17 else 17 - start_hour
                    on_hours = on_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 17 else 17
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "On Hours:", on_hours, "Time Charged:", time_charged,
                    #     "Start Hour:", start_hour)

                if 17 <= start_hour < 19:
                    # print("17-19")
                    time_charged = total_hours_left if start_hour + total_hours_left < 19 else 19 - start_hour
                    mid_hours = mid_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 19 else 19
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Mid Hours:", mid_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

                if 19 <= start_hour < 24:
                    time_charged = total_hours_left if start_hour + total_hours_left < 24 else 24 - start_hour
                    off_hours = off_hours + time_charged
                    start_hour = start_hour if start_hour + total_hours_left < 24 else 0
                    total_hours_left = total_hours_left - time_charged
                    # print("Total Hours Left:", total_hours_left, "Off Hours:", off_hours, "Time Charged:",
                    # time_charged, "Start Hour:", start_hour)

            return str(round(on_hours, 3)) + ", " + str(round(off_hours, 3)) + ", " + str(round(mid_hours, 3))


determine_peak_distribution(time_stop[27], time_start[27])
# date_year['Peaks_Python'] = date_year.apply(lambda row: determine_peak(row))

df_open_transactions['On-Off-Mid-Distribution'] = \
    df_open_transactions.apply(lambda x: determine_peak_distribution(x['UTCTransactionStop'], x['UTCTransactionStart']),
                               axis=1)
print(df_open_transactions)
