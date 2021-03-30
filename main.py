from reading_data import data_meter_values, data_open_trans

df_open_transactions = data_open_trans()
df_meter_values = data_meter_values()

print(df_open_transactions.columns.values)
print(df_meter_values.columns.values)
# print(df_open_trans.describe(datetime_is_numeric=True, include="all").to_string())
print(df_open_transactions['TransactionStartTime'].head())
print(df_open_transactions['TransactionStopTime'].head())

print((df_open_transactions['StartCard'].nunique()))

print((df_open_transactions.groupby(['Day/Night']).sum()))
