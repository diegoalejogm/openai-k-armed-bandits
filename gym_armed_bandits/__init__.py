from gym.envs.registration import register

register(
    id='three-armed-bandits-v0',
    entry_point='gym_armed_bandits.envs:ArmedBanditsGaussian',
    kwargs={'num_bandits':3}
)

register(
    id='five-armed-bandits-v0',
    entry_point='gym_armed_bandits.envs:ArmedBanditsGaussian',
    kwargs={'num_bandits':5}
)

register(
    id='ten-armed-bandits-v0',
    entry_point='gym_armed_bandits.envs:ArmedBanditsGaussian',
    kwargs={'num_bandits':10}
)
