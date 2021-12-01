# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def day_one():
    count = 0;
    measurements = Buddy().readDataFromFile('input.in');

    for index, measurement in enumerate(measurements):
        if index > 0 and measurement > measurements[index - 1]:
            count += 1;
        else:
            pass;

    Buddy().outputAnswer("Answer is: " + str(count));

## 23 days until christmas 🎄🎄🎄🎄🎄
day_one();
