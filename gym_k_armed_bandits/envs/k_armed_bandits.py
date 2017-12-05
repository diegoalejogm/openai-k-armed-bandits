import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class KArmedBanditsEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, num_bandits):
        assert num_bandits > 0
        self.num_bandits = num_bandits
        self.min_action, self.max_action = 0, num_bandits-1
        self.action_space = range(self.min_action, self.max_action)
        self.reward_distributions = self.__generate_gaussian_reward_distributions__()

    def _step(self, action):
        # Assert action is valid
        assert self.__valid_action__(action)
        observation = None
        reward = self.reward_distributions[action]()
        done = False # KArmedBandits is non-episodal, so agent decides when to end.
        info = dict() # Empty dict
        return observation, reward, done, info

    def _reset(self):
        # TODO: Check if resseting distributions is desired behaviour
        pass

    def _render(self, mode='human', close=False):
        pass

    def __valid_action__(self, action):
        return int(action) < self.num_bandits

    def __generate_gaussian_reward_distributions__(self):
        # Default Gaussian pdfs with gaussian distributed mean
        mu, sigma = 0, 1
        means = np.random.normal(mu, sigma, self.num_bandits)
        return [ lambda : np.random.normal(mu_i) for mu_i in means ]
