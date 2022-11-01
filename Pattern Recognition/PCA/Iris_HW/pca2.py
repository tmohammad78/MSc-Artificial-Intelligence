import pandas as pandas
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
from numpy.linalg import eig
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


iris = datasets.load_iris()  # load dataset from sklrean

X = iris.data  # load features 
y = iris.target # load targets 
# In this line , we normilized data , like this : z = (x - u) / s
X_scaled = StandardScaler().fit_transform(X) 

target_names = { # type of targets
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

cov_matrix  = np.cov(X_scaled,rowvar=False,bias=False)
w,v = eig(cov_matrix) # values and vectors matrices

plt.bar(["e" + str(i+1) for i in range(len(w))], w)
plt.title("Eigenvalues")
plt.xlabel("Magnitude of the eigenvalue")

transformed = np.dot(X_scaled, v)
print(transformed.shape,'transformed shappe')

print(cov_matrix)
my_vector = v[:,:2] # Select Two eigen vector
print(my_vector)
print(my_vector.shape,'shape of my vector')
pca = PCA(n_components=2)
pca_features = pca.fit_transform(X_scaled)
number_of_data = np.cumsum(pca.explained_variance_ratio_ * 100)[-1]
print(number_of_data) ## 95.81

print("Shape before PCA:",X_scaled.shape) # Shape of the data before reduction (150, 4)
print("Shapre after PCA:",pca_features.shape) # Shape of data after PCA (150, 3)

plt.show()
pca_df = pd.DataFrame(data=pca_features,columns=["PC1","PC2"])

# mapping target names to the PCA features
pca_df['target'] = y
pca_df['target'] = pca_df['target'].map(target_names)

pca_df.head()
sns.set()
sns.lmplot(
    x='PC1',  
    y="PC2",
    data=pca_df, 
    hue='target', 
    fit_reg=False, 
    legend=True
    )
 
plt.title('2D PCA Graph')
plt.show()

