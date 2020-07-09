[under active development]

This repository contains a PIP package which is a modified version of the CartPole OpenAI environment. 

## Installation
Install [OpenAI gym](https://gym.openai.com/).

Then install this package:

```
git clone http://github.com/modanesh/gym_modified_cartpole.git
cd gym_modified_cartpole
sudo pip install -e .
```

## Usage
Python usage:
```
import gym
import gym_mod_cartpole

env = gym.make('CartPoleMod-v0')
```

## Environments
- [x] **CartPoleMod-v0**: have a wind from left to right (L2R). Changes 50% of the **left** actions to **noop**. 
- [x] **CartPoleMod-v1**: have a wind from right to left (R2L). Changes 50% of the **right** actions to **noop**. 
- [x] **CartPoleMod-v2**: there is a friction with the value of **2e-3** applied to the cart. 
- [x] **CartPoleMod-v3**: there is a friction with the value of **-2e-3** applied to the cart, which makes the surface slippery.
- [x] **CartPoleMod-v4**: anomaly added to the environment. At a random step between (100, 250), a wind from left to right (L2R) starts blowing, like **CartPoleMod-v0** case. 
- [x] **CartPoleMod-v5**: anomaly added to the environment. At a random step between (100, 250), a wind from right to left (R2L) starts blowing, like **CartPoleMod-v1** case.

## TODO
- [ ] Add new modifications to introduce new environments