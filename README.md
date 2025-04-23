# Bouncing Balls Test


This repository contains Python code to test the capabilities of different Large Language Models (LLMs) to complete a specific scripting task. The task is to write a Python program that shows 20 balls bouncing inside a spinning heptagon. The program should be implemented using a specified set of Python libraries.

## Task Description

The following are the requirements for the program:

1. **Balls and Heptagon:**
   - There are 20 balls inside a spinning heptagon.
   - All balls have the same radius.
   - Each ball has a unique number from 1 to 20.
   - The balls drop from the heptagon center when starting.
   - The heptagon spins at a rate of 360 degrees per 5 seconds.

2. **Ball Appearance:**
   - The balls have the following colors:
     - #f8b862
     - #f6ad49
     - #f39800
     - #f08300
     - #ec6d51
     - #ee7948
     - #ed6d3d
     - #ec6800
     - #ee7800
     - #eb6238
     - #ea5506
     - #ea5506
     - #eb6101
     - #e49e61
     - #e45e32
     - #e17b34
     - #dd7a56
     - #db8449
     - #d66a35

3. **Physics:**
   - The balls are affected by gravity and friction.
   - The balls should bounce off the rotating walls realistically.
   - Collisions between balls should be detected and responded to properly.
   - The impact bounce height of the balls will not exceed the radius of the heptagon but will be higher than the ball radius.
   - The balls rotate with friction, and the numbers on the balls can indicate the spin of the ball.

4. **Implementation Constraints:**
   - The heptagon size should be large enough to contain all the balls.
   - Do not use the `pygame` library; implement collision detection algorithms and collision response by yourself.
   - Allowed Python libraries: `tkinter`, `math`, `numpy`, `dataclasses`, `typing`, `sys`.
   - All codes should be put in a single Python file.
