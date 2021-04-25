from sklearn.cluster import DBSCAN
from reading_data import data_open_trans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)

start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))

print(df_open_transactions.columns.values)
df_open_transactions['ConnectedTime'] = pd.to_numeric(df_open_transactions['ConnectedTime'])
df_open_transactions = df_open_transactions[df_open_transactions['ConnectedTime'] <= 25]
data = df_open_transactions[['Start Integer Hour_P', 'ConnectedTime']]

plt.scatter(data['Start Integer Hour_P'], data['ConnectedTime'], s=2)
plt.title('Start Time and Total Connected Time')
plt.xlabel('Start Connection Hour ')
plt.ylabel('Total Hours Connected')
plt.show()

dbscan = DBSCAN(eps=0.9, min_samples=20).fit(data)
core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
core_samples_mask[dbscan.core_sample_indices_] = True
labels = dbscan.labels_
print(labels)

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Number of clusters through DBSCAN: ", n_clusters_)
print("Number of Noise points: ", n_noise_)

unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = data[class_member_mask & core_samples_mask]
    plt.plot(xy['Start Integer Hour_P'], xy['ConnectedTime'], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k',
             markersize=6, alpha=0.8)

    xy = data[class_member_mask & ~core_samples_mask]
    plt.plot(xy['Start Integer Hour_P'], xy['ConnectedTime'], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k',
             markersize=6, alpha=0.8)

plt.title('Estimated number of clusters through DBSCAN: %d' % n_clusters_)
plt.xlabel('Start Connection Hour ')
plt.ylabel('Total Hours Connected')
plt.show()
