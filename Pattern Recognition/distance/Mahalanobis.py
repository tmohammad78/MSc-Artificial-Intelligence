import numpy as np

A = np.array([[1, 3, 5], [5, 2, 0], [3, 8, 10]])

def calculateMahan ():
    cov_mat = np.cov(A,rowvar=False,bias=True)

    x_minus_mu = A - np.mean(A)
    inv_cov = np.linalg.inv(cov_mat)
    left_term = np.dot(x_minus_mu, inv_cov)
    mahal = np.dot(left_term, x_minus_mu.T)
    return mahal

print(calculateMahan())