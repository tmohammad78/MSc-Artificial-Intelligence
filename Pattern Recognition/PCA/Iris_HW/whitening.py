import numpy as np
 
#### for first question
def whitening(covx:np.ndarray):
    e_values, e_vectors = np.linalg.eigh(covx) # pass a cov matrix
    print("Eigenvalues:", e_values.real.round(4), '\n')
    print("Eigenvectors:", e_vectors, '\n')
    diagw = np.diag(1/(e_values**0.5)) # or np.diag(1/((w+.1e-5)**0.5))
    diagw = diagw.real.round(4)

    return np.dot(diagw, e_vectors.T)

print(whitening([[4,1],[1,5]]))



## Second question
def independence_normal_sample(count:int, dimension:int):
    covx = np.identity(dimension, dtype = int)
    mean = np.zeros(dimension)
    return np.random.multivariate_normal(mean, covx, count)

print(independence_normal_sample(2,5))


### part 3

def transform_s(data:np.ndarray, covx:np.ndarray):
    whited = whitening(covx)
    transformed_data = None
    for sample in data.T:
        transformed_sample = np.dot(whited, sample.T)
        if transformed_data is None: # first time
            transformed_data = transformed_sample
        else:
            transformed_data = np.column_stack((transformed_data,transformed_sample))
    return transformed_data

data = create_independence_normal_sample(2,5)
print(f"normal samples: {data}")

transformed_data = transform_s(data, np.array([[4,2],[2,5]]))
print(f"transformed_data: {transformed_data}")