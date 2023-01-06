

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

from sklearn.datasets import load_iris
from sklearn import preprocessing

dataset = load_iris()

# X.features= ie row names
# ['sepal length (cm)',     0
#  'sepal width (cm)',      1
#  'petal length (cm)',     2
#  'petal width (cm)']      3

X = pd.DataFrame(dataset.data)
y = pd.DataFrame(dataset.target)


colormap = np.array(['red', 'lime', 'black'])

# REAL PLOT
plt.subplot(1, 3, 1)
plt.scatter(X[2], X[3], c=colormap[y[0]])
plt.title('Real')

# K-PLOT
model = KMeans(n_clusters=3)
model.fit(X)
predY = model.predict(dataset.data)
plt.subplot(1, 3, 2)
plt.scatter(X[2], X[3], c=colormap[predY])
plt.title('KMeans')

# GMM PLOT
scaler = preprocessing.StandardScaler()
scaler.fit(X)
xsa = scaler.transform(X)
xs = pd.DataFrame(xsa)
gmm = GaussianMixture(n_components=3)
gmm.fit(xs)
gmmptrf = gmm.predict(xs)
plt.subplot(1, 3, 3)
plt.scatter(X[2], X[3], c=colormap[gmmptrf])
plt.title('GMM Classification')


plt.show()
