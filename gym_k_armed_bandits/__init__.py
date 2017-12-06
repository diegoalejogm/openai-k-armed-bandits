from gym.envs.registration import register

register(
    id='three-armed-bandits-v0',
    entry_point='gym_k_armed_bandits.envs:KArmedBanditsGaussian',
    kwargs={'num_bandits':3}
)

register(
    id='ten-armed-bandits-v0',
    entry_point='gym_k_armed_bandits.envs:KArmedBanditsGaussian',
    kwargs={'num_bandits':10}
)
