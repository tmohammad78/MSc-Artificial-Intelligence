# Imitation Learning 
Imitation learning is like RL but we have information and data from an expert and we want to imitate that behaviour.

Most IL work can be divided into two branches: Behavioral Cloning and Inverse Reinforcement Learning. **Behavioral Cloning** casts IL as a supervised learning objective and seeks to imitate the expert’s actions using the provided demonstrations as a fixed dataset.<br />
Thus, Behavioral Cloning usually requires a lot of expert data and results in agents that struggle to generalize. In this approach we have risk of compounding error, it means when agent deviates from the demonstrated behaviors risk of making errors increased. <br />
**Inverse Reinforcement Learning** aims to reduce compounding error by learning a reward function under which the expert policy is optimal.Once learned, an agent can be trained (with any RL algorithm) to learn how to act at any given state of the environment.<br />
To learn a reward function from the expert data, such that a policy that optimizes the reward through environment interaction matches the expert. <br />
Another approach is to use GANs (a class of generative models).In this way the agent policy model (the “generator”) produces actions interacting with an environment to attain the highest rewards from a reward model using RL, while the reward model (the “discriminator”) attempts to distinguish the agent policy behavior from expert behavior. Similar to GANs, the discriminator acts as a reward model that indicates how expert-like an action is.**if the policy does something that is not expert-like, it gets a low reward from the discriminator and learns to correct this behavior.** This method is called Adversarial Imitation.<br />
<br />

![RL](https://github.com/tmohammad78/MSc-Artificial-Intelligence/blob/main/Imitation%20Learning/images/Adversarial.png)

But it has many problems and it's so depend on hyperparameters. the process of reinforcement learning complicates training because it is not possible to train the generator here through simple gradient descent.

