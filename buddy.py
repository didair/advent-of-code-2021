# Advent of Code 2021
# Author: Andreas Ekström <didair>

class Buddy:

    # Read data from file, and return the data as array
    def readDataFromFile(self, filename):
        with open(filename) as f:
            data = [];
            for x in f.readlines():
                if (x.strip().isdigit()):
                    data.append(int(x.strip()));
                else:
                    data.append(x);

        return data;

    # Prints each argument and wraps it in a christmas-y theme
    def outputAnswer(self, *answers):
        print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄");

        for answer in answers:
            if type(answer) == str:
                print(answer);
            else:
                pass;

        print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄");
