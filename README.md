# Data-Analysis-EV-Charging-Dataset
Data Analysis of EV charging Dataset by [Elaad NL](https://elaad.nl/en/)

##Python Scripts:

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

`peak_distribution_TOU_7.py``: Specifically examines peak charging times under Time-of-Use (TOU) tariffs, potentially optimizing cost strategies.

`reading_data.py``: A utility script for reading and preprocessing data from provided datasets.

`regression_per_GMM_cluster.py``: Conducts regression analysis within each cluster defined by a prior GMM clustering process.

