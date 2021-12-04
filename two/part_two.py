# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def day_two():
    instructions = Buddy().readDataFromFile('input.in');

    aim = 0;
    horizontal = 0;
    depth = 0;

    for data in instructions:
        instruction = data.split(' ');
        command = instruction[0];
        value = int(instruction[1]);

        if (command == 'forward'):
            horizontal += value;
            depth += aim * value;

        if (command == 'up'):
            aim -= value;

        if (command == 'down'):
            aim += value;

    Buddy().outputAnswer(
        "Horizontal: " + str(horizontal),
        "Depth " + str(depth),
        "Aim " + str(aim),
        "Answer is: " + str(horizontal * depth)
    );

## 21 days until christmas 🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄
day_two();
