from sklearn.cluster import kmeans_plusplus
import matplotlib.pyplot as plt
import pandas as pd
from reading_data import data_open_trans
from datetime import datetime
import numpy as np


df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)

start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))

# print(df_open_transactions.columns.values)

# print(df_open_transactions['Start Integer Hour_P'])

data = df_open_transactions[['Start Integer Hour_P', 'ConnectedTime']]
y_true = df_open_transactions['ConnectedTime']
y_true = y_true.to_numpy()
data = data.to_numpy()
# print(data['Start Integer Hour_P'])
# print(data['ConnectedTime'])

# plt.scatter(data['Start Integer Hour_P'], data['ConnectedTime'], s=2)
# plt.title('Start Time and Total Connected Time')
# plt.xlabel('Start Connection Hour ')
# plt.ylabel('Total Hours Connected')
# plt.show()


print(type(data))
print(data.shape)
data = data[:, ::-1]
centers_init, indices = kmeans_plusplus(data, n_clusters=4, random_state=0)

print(centers_init, indices)
colors = ['#4EACC5', '#FF9C34', '#4E9A06', 'm']

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(data[cluster_data, 0], data[cluster_data, 1],
                c=col, marker='.', s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c='b', s=50)
plt.title("K-Means++ Initialization")
plt.xticks([])
plt.yticks([])
plt.show()
