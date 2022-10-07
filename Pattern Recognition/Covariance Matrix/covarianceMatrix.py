import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

A = np.array([[1, 3, 5], [5, 4, 1], [3, 8, 6]])
# Calculate covariance with numpy , just one line :)) 
covResult = np.cov(A,rowvar=False,bias=True) ## bias=True divides by n and not by n-1 and select colum by rowvar=False

def calculateCovariance(X):
    mean = np.mean(X,axis=0) # axis 0 means , you take each col.
    lenX = X.shape[0]
    X = X - mean
    return X.T.dot(X)/lenX

def plotDataAndCov(data):
    ACov = np.cov(data, rowvar=False, bias=True)
    print ('Covariance matrix:\n', ACov)

    fig, ax = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(10, 10)

    ax0 = plt.subplot(2, 2, 1)
    
    # Choosing the colors
    cmap = sns.color_palette("GnBu", 10)
    sns.heatmap(ACov, cmap=cmap, vmin=0)

    ax1 = plt.subplot(2, 2, 2)
    
    # data can include the colors
    if data.shape[1]==3:
        c=data[:,2]
    else:
        c="#0A98BE"
    ax1.scatter(data[:,0], data[:,1], c=c, s=40)
    
    # Remove the top and right axes from the data plot
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

calculateCovariance(A)
plotDataAndCov(A)
sns.distplot(A[:,0], color="#53BB04")
sns.distplot(A[:,1], color="#0A98BE")
plt.show()
plt.close()

np.random.seed(1234)
a1 = np.random.normal(2, 1, 300)
a2 = np.random.normal(1, 1, 300)
A = np.array([a1, a2]).T
A.shape
sns.distplot(A[:,0], color="#53BB04")
sns.distplot(A[:,1], color="#0A98BE")
plotDataAndCov(A)
plt.show()
plt.close()