import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='CartPoleMod-v0',
    entry_point='gym_mod_cartpole.envs:ModCartPoleEnv',
    kwargs={'case':0},
)
register(
    id='CartPoleMod-v1',
    entry_point='gym_mod_cartpole.envs:ModCartPoleEnv',
    kwargs={'case':1},
)