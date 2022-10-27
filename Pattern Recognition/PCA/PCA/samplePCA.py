import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd

mu = np.array([10,13])

sigma = np.array([[3.5,-1.8],
                  [-1.8,3.5]])

org_data = rnd.multivariate_normal(mu,sigma, size=(1000))
plt.figure("Figure 1")
plt.scatter(org_data[:,0],org_data[:,1]) 

print("Data is",org_data.shape)

mean = np.mean(org_data)
print("Mean is:",mean)

mean_data = org_data - mean
plt.figure("Figure 2")
plt.scatter(mean_data[:,0],mean_data[:,1]) 
print(mean_data.shape)
# plt.show()

cov_mt = np.cov(mean_data,rowvar=False,bias=False)
print(cov_mt.shape)

eig_val, eig_vec = np.linalg.eig(cov_mt)
print("Eigen vectors ", eig_vec)
print("Eigen values ", eig_val, "\n")

pca_data = np.dot(mean_data, eig_vec)
print("Transformed data ", pca_data.shape)

# Plot data

fig, ax = plt.subplots(1,3, figsize= (15,15))
# Plot original data
ax[0].scatter(org_data[:,0], org_data[:,1], color='blue', marker='.')

# Plot data after subtracting mean from data
ax[1].scatter(mean_data[:,0], mean_data[:,1], color='red', marker='.')

# Plot data after subtracting mean from data
ax[2].scatter(pca_data[:,0], pca_data[:,1], color='red', marker='.')

# Set title
ax[0].set_title("Scatter plot of original data")
ax[1].set_title("Scatter plot of data after subtracting mean")
ax[2].set_title("Scatter plot of transformed data")

# Set x ticks
ax[0].set_xticks(np.arange(-8, 1, 8))
ax[1].set_xticks(np.arange(-8, 1, 8))
ax[2].set_xticks(np.arange(-8, 1, 8))

# Set grid to 'on'
ax[0].grid('on')
ax[1].grid('on')
ax[2].grid('on')

major_axis = eig_vec[:,0].flatten()
xmin = np.amin(pca_data[:,0])
xmax = np.amax(pca_data[:,0])
ymin = np.amin(pca_data[:,1])
ymax = np.amax(pca_data[:,1])


recon_data = pca_data.dot(eig_vec.T) + mean
print(recon_data.shape)

fig, ax = plt.subplots(1,3, figsize= (15, 15))
ax[0].scatter(org_data[:,0], org_data[:,1], color='blue', marker='.')
ax[1].scatter(mean_data[:,0], mean_data[:,1], color='red', marker='.')
ax[2].scatter(recon_data[:,0], recon_data[:,1], color='red', marker='.')
ax[0].set_title("Scatter plot of original data")
ax[1].set_title("Scatter plot of data after subtracting mean")
ax[2].set_title("Scatter plot of reconstructed data")
ax[0].grid('on')
ax[1].grid('on')
ax[2].grid('on')
plt.show()


loss = np.mean(np.square(recon_data - org_data))
print("Reconstruction loss ", loss)