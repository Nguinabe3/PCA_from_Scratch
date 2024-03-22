import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris['data']
y = iris['target']


n_samples, n_features = X.shape

print('Number of samples:', n_samples)
print('Number of features:', n_features)

class PCA:

  def __init__(self,n_component):
    self.n_component=n_component

  def mean(self, X):
    return np.divide(np.sum(X,axis=0),X.shape[0])

  def std(self,X):
    return np.divide(np.sum((X-self.mean(X))**2,axis=0),X.shape[0]-1)**.5

  def Standardize_data(self,X):
    return (X-self.mean(X))/self.std(X)

  def covariance(self,X):
    return np.divide(X.T@X,X.shape[0]-1)

  def eig(self,m):
    eigen_values, eigen_vectors = np.linalg.eig(m)
    Eeigen_vectors = eigen_vectors.T[:self.n_component,]
    return Eeigen_vectors

  def fit(self,X):
    X=self.Standardize_data(X)
    m=self.covariance(X)
    v=self.eig(m)
    return v

  def transform(self,x):
    P=self.fit(X)
    new_x=X@P.T
    return new_x
  
my_pca = PCA(n_component=3)
my_pca.fit(X)
new_X = my_pca.transform(X)

plt.title(f"PC1 vs PC2")
plt.scatter(new_X[:, 0], new_X[:, 1], c=y)
plt.xlabel('PC1'); plt.xticks([])
plt.ylabel('PC2'); plt.yticks([])
plt.show()