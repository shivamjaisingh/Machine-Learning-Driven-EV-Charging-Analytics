from sklearn.cluster import kmeans_plusplus
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])
print(X.shape)
print(type(X))
centers, indices = kmeans_plusplus(X, n_clusters=2, random_state=0)
print(centers)

print(indices)

