import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import pandas as pd
from reading_data import data_open_trans
from sklearn.model_selection import cross_val_score

df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)

start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))

print(df_open_transactions.columns.values)

# print(df_open_transactions['Start Integer Hour_P'])
df_open_transactions['ConnectedTime'] = pd.to_numeric(df_open_transactions['ConnectedTime'])
df_open_transactions = df_open_transactions[df_open_transactions['ConnectedTime'] <= 25]
data = df_open_transactions[['Start Integer Hour_P', 'ConnectedTime']]

plt.scatter(data['Start Integer Hour_P'], data['ConnectedTime'], edgecolors='k',
            s=45, alpha=.8, c='royalblue')
plt.title('Start Time and Total Connected Time')
plt.xlabel('Start Connection Hour ')
plt.ylabel('Total Hours Connected')
plt.show()

n_components = 4
gmm = GaussianMixture(n_components=n_components, covariance_type='full', random_state=300140951).fit(data)

labels = gmm.predict(data)
print(labels)
frame = pd.DataFrame(data)
frame['cluster'] = labels
frame.columns = ['Start Integer Hour_P', 'ConnectedTime', 'cluster']

print(frame['cluster'].nunique())
# plotting results
color = ['lightgreen', 'yellow', 'deeppink', 'orange', 'magenta', 'yellow', 'black', 'orange', 'pink']
marker_r = ["*", "+", "x", "3", ".", "o", "p", "D", "2"]
for k in range(0, 4):
    data = frame[frame["cluster"] == k]
    print("shape: " + str(data.shape))
    x = data['Start Integer Hour_P'].to_numpy().reshape(-1, 1)
    y = data['ConnectedTime'].to_numpy()
    reg = LinearRegression().fit(x, y)
    y_pred = reg.predict(x)
    print("Prediction with: " + str(k) + str(reg.predict(np.array([[19]]))))
    print("Score :" + str(reg.score(x, y) * 100))

    plt.scatter(data['Start Integer Hour_P'], data['ConnectedTime'], c=color[k], edgecolors='k',
                s=50, alpha=.8)

plt.title('GMM Visualization with ' + str(n_components) + ' clusters of charging sessions')
plt.xlabel('Start Connection Hour ')
plt.ylabel('Total Hours Connected')
plt.show()

