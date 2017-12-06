import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class ArmedBanditsEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, reward_distributions):
        assert reward_distributions

        self.num_bandits = len(reward_distributions)
        # Action space = [0 ...  num_bandits-1]
        self.action_space = spaces.Discrete(self.num_bandits)
        # Observation space = []
        self.observation_space = spaces.Discrete(0)
        self.reward_distributions = reward_distributions

    def _step(self, action):
        # Assert action is valid
        assert self.action_space.contains(action)
        # KArmedBandits is stationary and non-episodal.
        info = dict() # Empty dict
        observation, done, info = None, False, dict()
        reward = self.reward_distributions[action]()
        return observation, reward, done, info

    def _reset(self):
        # TODO: Check if resseting distributions is desired behaviour
        pass

    def _render(self, mode='human', close=False):
        pass

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]


class ArmedBanditsGaussian(ArmedBanditsEnv):

    def __init__(self, num_bandits=3):
        distributions = self.__generate_gaussian_reward_distributions__(num_bandits)
        self.means = distributions[1]
        ArmedBanditsEnv.__init__(self, distributions[0])

    def __generate_gaussian_reward_distributions__(self, num_bandits):
        means = np.random.normal(0, 1, size=num_bandits)
        distributions = [ lambda : np.random.normal(mu_i) for mu_i in means ]
        return distributions, means
