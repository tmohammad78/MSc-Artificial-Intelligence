import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./mnist.csv")

def show_number():
    second_image = data.iloc[6].values.reshape([28,28])
    plt.imshow(second_image, cmap='gray_r')
    plt.title('Second image: Digit 0', fontsize=15, pad=15)
    plt.savefig("Second image.png")
    plt.show()

print(data.head()) # show head of data 
# we don't need to label col , so we drop it
data.drop(columns="label",inplace=True)
print(data.head()) # show head of data 
show_number()

cova = np.cov(data,rowvar=False,bias=True)
print(cova)