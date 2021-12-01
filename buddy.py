# Advent of Code 2021
# Author: Andreas Ekström <didair>

import csv

class Buddy:

    def __init__(self, options):
        self.options = options;

    # Read data from file, and return the data as array 
    def readDataFromCSV(file):
        with open(file) as f:
            data = f.read().splitlines();
            return data;

    # Prints each argument and wraps it in a christmas-y theme
    def outputAnswer(*answers):
        print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄");

        for answer in answers:
            if answer is not None
                print(answer);
            else:
                pass;

        print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄");
