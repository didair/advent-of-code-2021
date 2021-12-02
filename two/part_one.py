# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def day_two():
    instructions = Buddy().readDataFromFile('input.in');

    horizontal = 0;
    depth = 0;

    for data in instructions:
        instruction = data.split(' ');
        command = instruction[0];
        value = int(instruction[1]);

        if (command == 'forward'):
            horizontal += value;

        if (command == 'up'):
            depth -= value;

        if (command == 'down'):
            depth += value;

    Buddy().outputAnswer(
        "Horizontal: " + str(horizontal),
        "Depth " + str(depth),
        "Answer is: " + str(horizontal * depth)
    );

## 22 days until christmas 🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄
day_two();
