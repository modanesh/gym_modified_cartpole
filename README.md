[under active development]

This repository contains a PIP package containing modified versions of control tasks of OpenAI gym. 

## Installation
Install [OpenAI gym](https://gym.openai.com/).

Then install this package:

```
git clone http://github.com/modanesh/modified_gym.git
cd modified_gym
sudo pip install -e .
```

## Usage
Python usage:
```
import gym
import modified_gym

env = gym.make('CartPoleMod-v0')
```

## Environments
- [x] **CartPoleMod-v0**: has a wind from left to right (L2R). Changes 50% of the **left** actions to **noop**. 
- [x] **CartPoleMod-v1**: has a wind from right to left (R2L). Changes 50% of the **right** actions to **noop**. 
- [x] **CartPoleMod-v2**: there is a friction with the value of **2e-3** applied to the cart. 
- [x] **CartPoleMod-v3**: there is a friction with the value of **-2e-3** applied to the cart, which makes the surface slippery.
- [x] **CartPoleMod-v4**: at a random step between (100, 250), a wind from left to right (L2R) starts blowing, like **CartPoleMod-v0** case. 
- [x] **CartPoleMod-v5**: at a random step between (100, 250), a wind from right to left (R2L) starts blowing, like **CartPoleMod-v1** case.
- [x] **CartPoleMod-v6**: has winds from left to right (L2R) and right to left (R2L). Changes 75% of the **left** or **right** actions to **noop**.
- [x] **CartPoleMod-v7**: at a specific step (100), a very small and gradual wind from both sides start. Changes actions forces to a fraction of them.
- [x] **CartPoleMod-v8**: at specific steps depending on horizon, a sudden and big wind from both sides blow. Multiplies and negates actions forces.
- [x] **AcrobotMod-v0**: has a wind from left to right (L2R). Changes 75% of the **left** actions to **noop**. 
- [x] **AcrobotMod-v1**: has a wind from right to left (R2L). Changes 75% of the **right** actions to **noop**. 
- [x] **LunarLanderMod-v0**: has a wind upwards. Changes 33% of the **main engine fire** actions to **noop**. 
- [x] **LunarLanderMod-v1**: has a wind from the sides. Changes 66% of the **left/right engine fire** actions to **noop**. 
- [x] **LunarLanderMod-v2**: has a combination of winds: upwards and from the sides. Changes 33% of the **main engine fire** and 66% of the **left/right engine fire** actions to **noop**. 
- [x] **MountainCarMod-v2**: has a combination of winds: from left to right (L2R) and right to left (R2L). Changes 75% of the **left** or **right** actions to **noop**. 

## TODO
- [ ] Add new modifications to introduce new environments