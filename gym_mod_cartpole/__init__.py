import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='CartPoleMod-v0',
    entry_point='gym_mod_cartpole.envs:ModCartPoleEnv',
    kwargs={'case':0, 'max_episode_steps':500},
)
register(
    id='CartPoleMod-v1',
    entry_point='gym_mod_cartpole.envs:ModCartPoleEnv',
    kwargs={'case':1, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v2',
    entry_point='gym_mod_cartpole.envs:ModCartPoleEnv',
    kwargs={'case':2, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v3',
    entry_point='gym_mod_cartpole.envs:ModCartPoleEnv',
    kwargs={'case':3, 'max_episode_steps':500}
)