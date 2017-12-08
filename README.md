# openai-k-armed-bandits

This repository contains an easy-to-use OpenAI Gym environment to train your agents with the famously known k-Armed-Bandits Reinforcement Learning task. You can check out a working example of an agent using this environment in my [Reinforcement Learning Book Exercices Repository.](https://github.com/diegoalejogm/Reinforcement-Learning/blob/master/Chapter%202/Playground%20Notebook.ipynb). 

## Install

There are two ways to install this project. The easiest procedure is using `pip` to download the project from [PyPi](http://pypi.python.org/) by typing in your terminal:

```pip install gym_armed_bandits```

An alternative way is by downloading the repository directly and installing the package locally:

```
git clone gym_armed_bandits
cd gym_armed_bandits
pip install -e .
```
This second method allows you to develop on the repository and instantly see the changes when importing. This is useful when contributing to this repository.

## Use

In your Python scripts the libraries
```
import gym
import gym_armed_bandits
```

and then load a specific environment by running
```
env = gym.make(<environment name>)
```
e.g.
```
env = gym.make('ten-armed-bandits-v0')
```

Currently the existing environments available in this project are:

- three-armed-bandits-v0
- five-armed-bandits-v0
- ten-armed-bandits-v0

All of these environments have bandits with std=1 gaussian distributions.

The code is implemented in such a way that it is easy to add a new bandit.


## License
MIT




