# ML Driven Analytics of EV charging Dataset by [Elaad NL](https://elaad.nl/en/)

## Python Scripts Description

`RandomForest_ChargeTime_Summer.py`: This script utilizes the Random Forest regression model to predict the charging time of EVs during the summer months based on historical data.

`RandomForest_ChargeTime_Winter.py`: Similar to its summer counterpart, this script predicts the charging time for EVs during the winter, using a Random Forest regression model.

`RandomForest_EnergyConsumption_Summer.py`: This script predicts the energy consumption of EVs in the summer using the Random Forest regression model.

`RandomForest_EnergyConsumption_Winter.py`: It forecasts winter energy consumption by EVs with the Random Forest regression model, adjusting for seasonal variables.

`RandomForest_IdleTimeRatio_Summer.py`: Predicts the ratio of idle time at charging stations during the summer months using Random Forest.

`RandomForest_IdleTimeRatio_Winter.py`: Uses Random Forest to estimate the winter idle time ratio, which is crucial for managing charging station availability.

`XGBoost_ChargeTime_Summer.py`: Applies the XGBoost regression model to predict the charge time for EVs in the summer.

`XGBoost_ChargeTime_Winter.py`: Uses XGBoost to model and predict the charging time for EVs during winter.

`XGBoost_EnergyConsumption_Summer.py`: Predicts the energy consumption for EVs in the summer using XGBoost, known for its efficiency and accuracy.

`XGBoost_EnergyConsumption_Winter.py`: This script is aimed at forecasting energy consumption in winter using the XGBoost model.

`XGBoost_IdleTimeRatio_Summer.py`: Uses XGBoost to predict the summer idle time ratio at EV charging stations.

`XGBoost_IdleTimeRatio_Winter.py`: Predicts winter idle time ratios using the XGBoost model, helping optimize station usage.

`bic_dbscan.py`: Estimates the optimal parameters for DBSCAN clustering using the Bayesian Information Criterion (BIC), a criterion for model selection.

`dbscan_clustering.py`: Implements the DBSCAN clustering algorithm to identify patterns or groups in EV charging data.

`elbow_kmeans_plus_plus.py`: Uses the "elbow method" to determine the optimal number of clusters for the K-means++ clustering algorithm.

`gmm_clustering.py`: Applies Gaussian Mixture Models (GMM) for clustering the data, providing a probabilistic model for the grouping.

`lin_regression_energy.py`: This script performs linear regression to model the relationship between variables influencing energy consumption.

`main.py`: Serves as the central script to run analyses or coordinate the execution of other scripts.

`peak_distribution.py`: Analyzes the distribution of peak charging times across different periods.

`peak_distribution_TOU_7.py`: Specifically examines peak charging times under Time-of-Use (TOU) tariffs, potentially optimizing cost strategies.

`reading_data.py`: A utility script for reading and preprocessing data from provided datasets.

`regression_per_GMM_cluster.py`: Conducts regression analysis within each cluster defined by a prior GMM clustering process.

## Few of the output visuals

![Idle-Time-Ratio-hour-all](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/308e6168-7d7f-4067-a148-08870e72680d)

This line graph shows the average idle time ratio per hour of the day across all seasons. The x-axis represents the time of the day, while the y-axis indicates the idle time ratio, which is the proportion of time EV chargers are plugged in but not actively charging. The graph reveals two prominent peaks around midnight and 8 PM, indicating higher idle times during these periods, and a notable dip around noon, suggesting more active charging during midday hours.

![kmeans_plus_plus with 5](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/42c75177-64ea-41c7-b42f-d4f135bfd192)

This scatter plot shows the results of applying the K-Means++ clustering algorithm with five clusters to the EV charging dataset. The x-axis represents the start connection hour, and the y-axis indicates the total hours connected. The data points are color-coded into five clusters: yellow, pink, green, orange, and purple, each representing distinct patterns of EV charging behavior based on the time of connection and the duration of connection, highlighting more granular groupings compared to the three-cluster solution.

![scatter_energy](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/93db248b-6710-4649-8cf8-685e43921709)

This scatter plot illustrates the relationship between the start connection hour and the total energy units consumed for EV charging sessions. The x-axis represents the start connection hour, ranging from 0 to 24 hours, while the y-axis shows the total energy units consumed. The plot indicates a wide distribution of energy consumption across different start times, with no clear trend or correlation between the start hour and the total energy units consumed, suggesting that energy consumption is fairly consistent regardless of the start time.

![trans_day_night](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/6810210c-c471-4736-bc22-c0d3614d9f8f)

This image is a histogram showing the distribution of EV charging transactions across different hours of the day, divided into day and night periods. The x-axis represents the starting hour of the transaction, while the y-axis shows the number of transactions. The chart indicates a high frequency of transactions starting in the early morning hours, with a significant decline as the day progresses.

![table-for-orange](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/77a30e88-1508-43bb-8ac4-fc828a4a9cad)

This table displays the predicted total energy consumption (in kilowatt-hours) for EV charging sessions that start at various hours of the day for a cluster labeled "orange." The "Connection Start Hour" column lists the hours from midnight (0.0) to noon (12.0), while the "Total Energy predicted" column shows the corresponding predicted energy consumption. The data indicates a slight decrease in predicted energy consumption as the start hour moves from midnight through the late morning, with the highest energy consumption predicted at midnight and the lowest at noon.

![Energy-demand-vs-predicted color deeppink](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/b4f67cab-c53d-4276-b5e8-1b237393615a)

This line graph compares the average energy demand to the predicted energy for a cluster labeled "deeppink." The x-axis represents the start connection hour, while the y-axis shows the average energy demand and predicted energy in kilowatt-hours (kWh). The graph indicates that the predicted energy (in pink) generally aligns with the actual energy demand (in black), showing a decreasing trend in energy usage as the start connection hour progresses from morning to evening, with some minor deviations between the actual and predicted values.

![count_weekday_all](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/085a901a-aa0d-4f74-ae3d-66fdb94b6be7)

This bar chart depicts the number of EV charging transactions per day of the week, aggregated across all seasons. The x-axis represents the days of the week, while the y-axis shows the total number of transactions. The chart indicates that Saturday has the highest number of transactions, followed by Tuesday and Friday, while Sunday has the lowest, suggesting higher EV charging activity on weekends and mid-week.

![AIC and BIC Curves for GMM](https://github.com/shivamjaisingh/ML-Driven-EV-Charge-Analytics/assets/20377780/569a6b17-9cc5-431a-ba5d-aefdb1e7d3fc)

This plot shows the Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) curves for evaluating the Gaussian Mixture Model (GMM) with different numbers of components (clusters). The x-axis represents the number of components, while the y-axis shows the AIC and BIC values. Both curves initially decline sharply, indicating improved model fit with increasing components, and then level off, suggesting the optimal number of clusters is around 10 to 15, where both AIC and BIC values reach their minimum or stabilize.











