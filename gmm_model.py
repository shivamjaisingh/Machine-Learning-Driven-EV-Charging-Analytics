from sklearn.mixture import GaussianMixture
from datetime import datetime
import pandas as pd
import numpy as np
from reading_data import data_open_trans

df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)

start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))

print(df_open_transactions.columns.values)

# print(df_open_transactions['Start Integer Hour_P'])

data = df_open_transactions[['Start Integer Hour_P', 'ConnectedTime']]


gmm = GaussianMixture(n_components=2, covariance_type='full').fit(data)
