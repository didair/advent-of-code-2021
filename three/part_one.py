# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def day_three():
    report = [];
    with open('input.in') as file:
        report = file.read().splitlines();

    gamma = "";
    epsilon = "";

    for i in range(len(report[0])):
        column = "";

        for index, line in enumerate(list(report)):
            column += str(line[i]);

        if column.count("1") > column.count("0"):
            gamma += "1";
            epsilon += "0";
        else:
            gamma += "0";
            epsilon += "1";

    Buddy().outputAnswer(
        "Gamma " + gamma,
        "Epsilon " + epsilon,
        "Answer is: " + str(int(gamma, 2) * int(epsilon, 2)),
    );

## 20 days until christmas 🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄
day_three();
