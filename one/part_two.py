# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def day_one():
    measurements = Buddy().readDataFromFile('input.in');

    count = 0;
    sliding_windows = [];

    for index in range(1, len(measurements)):
        sliding_windows.append(measurements[index-1:index+2]);

    for index, window in enumerate(sliding_windows):
        if sum(window) > sum(sliding_windows[index - 1]):
            count += 1;
        else:
            pass;

    Buddy().outputAnswer("Answer is: " + str(count));

## 23 days until christmas 🎄🎄🎄🎄🎄
day_one();
