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
- [x] **CartPoleMod-v0**: has a wind simulation from left to right (L2R). Changes 50% of the **left** actions to **noop**. 
- [x] **CartPoleMod-v1**: has a wind simulation from right to left (R2L). Changes 50% of the **right** actions to **noop**. 
- [x] **CartPoleMod-v2**: there is a friction simulation with the value of **2e-3** applied to the cart. 
- [x] **CartPoleMod-v3**: there is a friction simulation with the value of **-2e-3** applied to the cart, which makes the surface slippery.
- [x] **CartPoleMod-v4**: at a random step between (100, 250), a simulation of wind from left to right (L2R) starts, like **CartPoleMod-v0** case. 
- [x] **CartPoleMod-v5**: at a random step between (100, 250), a simulation of wind from right to left (R2L) starts, like **CartPoleMod-v1** case.
- [x] **CartPoleMod-v6**: has simulations of wind from left to right (L2R) and right to left (R2L). Changes 75% of the **left** or **right** actions to **noop**.
- [x] **CartPoleMod-v7**: at a specific step (400), a simulation of a very small and gradual wind from both sides starts. Changes actions forces to a fraction of them.
- [x] **CartPoleMod-v8**: at specific steps depending on horizon, a simulation of a sudden and big wind from both sides starts. Multiplies and negates actions forces.
- [x] **AcrobotMod-v0**: has a simulation of of a wind from left to right (L2R). Changes 75% of the **left** actions to **noop**. 
- [x] **AcrobotMod-v1**: has a simulation of of a wind from right to left (R2L). Changes 75% of the **right** actions to **noop**. 
- [x] **AcrobotMod-v7**: at a specific step (40), a simulation of a very small and gradual wind from both sides starts. Changes actions forces to a fraction of them.
- [x] **AcrobotMod-v8**: at specific steps depending on horizon, a simulation of a sudden and big wind from both sides starts. Multiplies and negates actions forces.
- [x] **LunarLanderMod-v0**: has a simulation of upward wind. Changes 33% of the **main engine fire** actions to **noop**. 
- [x] **LunarLanderMod-v1**: has a simulation of winds from the sides. Changes 66% of the **left/right engine fire** actions to **noop**. 
- [x] **LunarLanderMod-v2**: has a simulation of combined winds: upwards and from the sides. Changes 33% of the **main engine fire** and 66% of the **left/right engine fire** actions to **noop**. 
- [x] **MountainCarMod-v2**: has a simulation of combined winds: from left to right (L2R) and right to left (R2L). Changes 75% of the **left** or **right** actions to **noop**. 

## TODO
- [ ] Add new types of anomalies to introduce environments with different dynamics