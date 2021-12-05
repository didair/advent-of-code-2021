# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def find_common_bit(pos, report):
    column = '';
    for index, line in enumerate(list(report)):
        column += str(line)[pos];

    if column.count("1") == column.count("0"):
        return 'e';

    if column.count("1") > column.count("0"):
        return '1';

    if column.count("0") > column.count("1"):
        return '0';

def get_oxygen(report):
    remaining = report;

    for column in range(len(report[0])):
        common = find_common_bit(column, remaining);

        if common == 'e':
            remaining = list(filter(lambda line: line[column] == '1', remaining));
        else:
            remaining = list(filter(lambda line: line[column] == common, remaining));

        if len(remaining) == 1:
            return remaining[0];

def get_scrubber(report):
    remaining = report;

    for column in range(len(report[0])):
        common = find_common_bit(column, remaining);

        if common == 'e':
            remaining = list(filter(lambda line: line[column] == '0', remaining));
        else:
            remaining = list(filter(lambda line: line[column] != common, remaining));

        if len(remaining) == 1:
            return remaining[0];

def day_three():
    report = [];
    with open('input.in') as file:
        report = file.read().splitlines();

    oxygen = get_oxygen(report);
    scrubber = get_scrubber(report);

    Buddy().outputAnswer(
        "Oxygen: " + str(oxygen),
        "Scrubber: " + str(scrubber),
        "Answer is: " + str(int(oxygen, 2) * int(scrubber, 2)),
    );

## 20 days until christmas 🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄
day_three();
