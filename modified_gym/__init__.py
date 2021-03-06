import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='CartPoleMod-v0',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':0, 'max_episode_steps':500},
)
register(
    id='CartPoleMod-v1',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':1, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v2',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':2, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v3',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':3, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v4',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':4, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v5',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':5, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v6',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':6, 'max_episode_steps':500}
)

register(
    id='CartPoleMod-v7',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':7, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v8',
    entry_point='modified_gym.envs:ModCartPoleEnv',
    kwargs={'case':8, 'max_episode_steps':500}
)
register(
    id='AcrobotMod-v0',
    entry_point='modified_gym.envs:ModAcrobotEnv',
    kwargs={'case':0}
)
register(
    id='AcrobotMod-v1',
    entry_point='modified_gym.envs:ModAcrobotEnv',
    kwargs={'case':1}
)
register(
    id='AcrobotMod-v7',
    entry_point='modified_gym.envs:ModAcrobotEnv',
    kwargs={'case':7}
)
register(
    id='AcrobotMod-v8',
    entry_point='modified_gym.envs:ModAcrobotEnv',
    kwargs={'case':8}
)
register(
    id='LunarLanderMod-v0',
    entry_point='modified_gym.envs:ModLunarLanderEnv',
    kwargs={'case':0}
)
register(
    id='LunarLanderMod-v1',
    entry_point='modified_gym.envs:ModLunarLanderEnv',
    kwargs={'case':1}
)
register(
    id='LunarLanderMod-v2',
    entry_point='modified_gym.envs:ModLunarLanderEnv',
    kwargs={'case':2}
)
register(
    id='LunarLanderMod-v7',
    entry_point='modified_gym.envs:ModLunarLanderEnv',
    kwargs={'case':7}
)
register(
    id='LunarLanderMod-v8',
    entry_point='modified_gym.envs:ModLunarLanderEnv',
    kwargs={'case':8}
)
register(
    id='MountainCarMod-v2',
    entry_point='modified_gym.envs:ModMountainCarEnv',
    kwargs={'case':2}
)