from gym.envs.registration import register

register(
    id='k-armed-bandits-v0',
    entry_point='gym_k_armed_bandits.envs:KArmedBanditsEnv',
    kwargs={'num_bandits':3}
)
