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
- [x] **CartPoleMod-v0**: have a wind from left to right (L2R). Changes 50% of the **left** actions to **noop**. 
- [x] **CartPoleMod-v1**: have a wind from right to left (R2L). Changes 50% of the **right** actions to **noop**. 
- [x] **CartPoleMod-v2**: there is a friction with the value of **2e-3** applied to the cart. 
- [x] **CartPoleMod-v3**: there is a friction with the value of **-2e-3** applied to the cart, which makes the surface slippery.
- [x] **CartPoleMod-v4**: at a random step between (100, 250), a wind from left to right (L2R) starts blowing, like **CartPoleMod-v0** case. 
- [x] **CartPoleMod-v5**: at a random step between (100, 250), a wind from right to left (R2L) starts blowing, like **CartPoleMod-v1** case.
- [x] **CartPoleMod-v6**: have winds from left to right (L2R) and right to left (R2L). Changes 75% of the **left** or **right** actions to **noop**.
- [x] **AcrobotMod-v0**: have a wind from left to right (L2R). Changes 75% of the **left** actions to **noop**. 
- [x] **AcrobotMod-v1**: have a wind from right to left (R2L). Changes 75% of the **right** actions to **noop**. 
- [x] **LunarLanderMod-v0**: have a wind upwards. Changes 33% of the **main engine fire** actions to **noop**. 
- [x] **LunarLanderMod-v1**: have a wind from the sides. Changes 66% of the **left/right engine fire** actions to **noop**. 
- [x] **LunarLanderMod-v2**: have a combination of winds: upwards and from the sides. Changes 33% of the **main engine fire** and 66% of the **left/right engine fire** actions to **noop**. 
- [x] **MountainCarMod-v2**: have a combination of winds: from left to right (L2R) and right to left (R2L). Changes 75% of the **left** or **right** actions to **noop**. 

## TODO
- [ ] Add new modifications to introduce new environments