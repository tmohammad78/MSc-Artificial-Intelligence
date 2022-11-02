import pandas as pandas
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
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

df = pd.DataFrame(iris.data,columns=iris.feature_names)
df["target"] = iris.target
df["target_names"] = df["target"].map(target_names)
# sns.countplot(x="target_names",data=df) # To show count of targets base type of them
# plt.title("Iris targets value count")
# # plt.show()


pca = PCA(n_components=3)
pca_features = pca.fit_transform(X_scaled)

print("Shape before PCA:",X_scaled.shape) # Shape of the data before reduction (150, 4)
print("Shapre after PCA:",pca_features.shape) # Shape of data after PCA (150, 3)

pca_df = pd.DataFrame(data=pca_features,columns=["PC1","PC2","PC3"])

# mapping target names to the PCA features
pca_df['target'] = y
pca_df['target'] = pca_df['target'].map(target_names)


# Bar plot of explained_variance
plt.bar(
    range(1,len(pca.explained_variance_)+1),
    pca.explained_variance_ratio_*100
    )

    # plt.bar(
    # range(1,len(pca.explained_variance_)+1),
    # pca.explained_variance_
    # )

print(
    f"""
    each eigenvector explained variance: {pca.explained_variance_}
    each eigenvector explained variance ratio: {pca.explained_variance_ratio_ *100}
    """
)

plt.xlabel('PCA Feature')
plt.ylabel('Explained variance')
plt.title('Feature Explained Variance')
plt.show()
plt.plot(
    range(1,len(pca.explained_variance_ )+1),
    np.cumsum(pca.explained_variance_),
    c='red',
    label='Cumulative Explained Variance')
 
plt.legend(loc='upper left')
plt.xlabel('Number of components')
plt.ylabel('Explained variance (eignenvalues)')
plt.title('Scree plot')
 
 
plt.show()