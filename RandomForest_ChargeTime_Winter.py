import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import pandas as pd
from reading_data import data_open_trans
import matplotlib.patheffects as pe
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# from sklearn.model_selection import cross_val_score

df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)

start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))

print(df_open_transactions.columns.values)

df_open_transactions['ConnectedTime'] = pd.to_numeric(df_open_transactions['ConnectedTime'])
df_open_transactions = df_open_transactions[df_open_transactions['ConnectedTime'] <= 24]
df_open_transactions = df_open_transactions[df_open_transactions['Season'] == 'Winter']

print(df_open_transactions.head(10))
print('The shape of our features is:', df_open_transactions.shape)

df_open_transactions = df_open_transactions[
    ['TotalEnergy', 'Season', 'ConnectedTime', 'Day of the Week', 'MaxPower', 'ChargeTime']]

df_open_transactions = pd.get_dummies(df_open_transactions)

label = np.array(df_open_transactions['ChargeTime'])

df_open_transactions = df_open_transactions.drop('ChargeTime', axis=1)

feature_list = list(df_open_transactions.columns)

df_open_transactions = np.array(df_open_transactions)

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(df_open_transactions, label, test_size=0.25,
                                                                            random_state=42)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)


rf = RandomForestRegressor(n_estimators=1000, random_state=42)

rf.fit(train_features, train_labels)

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Results for Charge Time (Winter)')
print('Mean Absolute Error:', round(np.mean(errors), 2))

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')