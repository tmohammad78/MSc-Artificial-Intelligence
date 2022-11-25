import os
import time

# data science imports
import math
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import fuzz
# visualization imports
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

## Read Data 
df_movies = pd.read_csv(
    "data/ml-latest/movies.csv",
    usecols=['movieId', 'title'],
    dtype={'movieId': 'int32', 'title': 'str'})

df_ratings = pd.read_csv(
    "data/ml-latest/ratings.csv",
    nrows=1000000,
    usecols=['userId', 'movieId', 'rating'],
    dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})


print('movies information: \n',df_movies.info())
print('Head information of movies: \n',df_movies.head())

## Create Data frame
df_ratings_cnt_tmp = pd.DataFrame(df_ratings.groupby('rating').size(), columns=['count'])

print("df_ratings_cnt_tmp: \n",df_ratings_cnt_tmp)