# Project Hints 
I want to document things that I've learned related to running a Machine learning project.

## Hyperparameters

## Hyperparameters Tuning
https://blog.floydhub.com/guide-to-hyperparameters-search-for-deep-learning-models/ <br />
https://towardsdatascience.com/hyperparameter-tuning-c5619e7e6624 <br />
https://neptune.ai/blog/hyperparameter-tuning-in-python-complete-guide <br />

## Batches 
When we have a large dataset it's a bad idea to load the whole of that dataset to the model because it gets a lot of memory another reason is this approach reduces the speed of training because in each training. The model updates the hyperparameters (weights and bias) only after passing through the whole data set. The model updates the hyperparameters after completing each batch and it has better speed. <br />
### Different  gradient descent algorithms based on batch size
1. Stochastic gradient descent is when we have a batch for every item in the dataset. for instance, we have 1000 images and we create 1000 batches (every image is a batch )
2. Batch gradient algorithm
    We have just one batch, for 1000 images we have just one batch
3. Mini Batch gradient descent 
    In this algorithm, the size of the batch is greater than one and less than the total size of the data set. we usually use 32 or 64.

## Epoches

### Seed 
we use seeds when we are setting random numbers, we don't want to get new random numbers again and again. because it causes our model be aware of data, and by running multi times, we see most of the data, so we use seeds to use the same random numbers again and again. <br />
```
from sklearn import datasets
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
X = iris.data
y = iris.target
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

```
The parameter random_state=42 sets the random seed to the same value every time you run the above code. This implies that you get the same validation set (X_test, y_test) every time you execute the above code. In this manner, if you change your model by either changing hyperparameters or ML algorithms and retrain it, you can be assured that any differences happen due to the changes to the model, and not due to having a different random validation set. <br />
The seed value is used to generate the random number generator. And, every time you use the same seed value, you will get the same random values.


## Monitoring Hypterparameters
For monitoring these parameters and sth like loss function or reward and etc , we can use ```Tensorboard``` or other packages like ```wandb```. <br />
https://neptune.ai/blog/how-to-manage-track-visualize-hyperparameters <br />
https://www.tensorflow.org/tensorboard <br />
https://wandb.ai/

## Save Model
One of the useful things that makes easier to see result our model without training model again, is try to save model and just for next time try to load that file in the model. <br />
There are some ways to do, one of them is using ```model.save('path/to/location')``` it create a **H5** file that allows to re-create the model, it saves hyperparameters and etc. <br />
Another way is to extract data as **.pkl** file, like this ```pickle.dump(model, open('model.pkl', 'wb'))``` . <br />
After all we can load the file and our model in it. <br />
```model = keras.models.load_model('path/to/location')``` <br />

https://stackoverflow.com/questions/55937713/difference-between-h5py-file-and-pickle-file-in-saving-a-model <br />
https://stackoverflow.com/questions/21752259/python-why-pickle <br />
https://practicaldatascience.co.uk/machine-learning/how-to-save-and-load-machine-learning-models-using-pickle <br />
https://www.tensorflow.org/guide/keras/save_and_serialize <br />


## Enviroment
Enviroment used in the RL projects, In RL we have some important parts, one of them is enviroment, for having enviroment we can use a library as name **Gymnasium**. <br />
There are many enviroments like: 

1. Classis Enviroment: Cart Pole , Acrobot , Mountain Car , Pendulum
2. Multi-Joint dynamics with Contact (aka MuJoCo): Ant, Walker
3. Atari: Adventure, Alien

```
import gymnasium as gym
env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()

```
https://github.com/Farama-Foundation/Gymnasium








### Recourse
1. https://vitalflux.com/why-use-random-seed-in-machine-learning/#:~:text=Conceptually%2C%20the%20seed%20value%20is,get%20the%20same%20random%20values.