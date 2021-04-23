from sklearn.cluster import DBSCAN
from datetime import datetime
from reading_data import data_open_trans

df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)
