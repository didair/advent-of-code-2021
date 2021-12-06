# Advent of Code 2021
# Author: Andreas Ekström <didair>

import sys
sys.path.append("..");

from buddy import Buddy

def check_row(row, draw_numbers):
    matches = 0;

    for number in row:
        if number in draw_numbers:
            matches += 1;

    if matches == len(row):
        return True;
    else:
        return False;

def check_column(board, draw_numbers):
    for column in range(len(board[0])):
        matches = 0;
        for row in board:
            if row[column] in draw_numbers:
                matches += 1;

        if matches == len(board[0]):
            return True;

    return False;

def check_bingo(board, draw_numbers):
    for row in board:
        if check_row(row, draw_numbers):
            return True;

    return check_column(board, draw_numbers);

def day_four():
    draw_numbers = [];
    raw_boards = [];
    boards = [];

    with open('input.in') as file:
        for line in file.read().splitlines():
            if ',' in line:
                draw_numbers = line.split(',');
            else:
                raw_boards.append(line);

    board = [];
    for index, line in enumerate(list(raw_boards)):
        if line == '' and board != []:
            boards.append(board);
            board = [];
        else:
            new_row = line.strip().replace('  ', ' ');

            if new_row != '':
                new_row = new_row.split(' ');
                board.append(new_row);

                if index == len(raw_boards) - 1:
                    boards.append(board);

    drawed_numbers = [];
    winning_boards = [];
    unmarked_score = 0;

    for number in draw_numbers:
        drawed_numbers.append(number);

        for index, board in enumerate(list(boards)):
            if check_bingo(board, drawed_numbers):
                if index not in winning_boards:
                    winning_boards.append(index);

        if len(winning_boards) == len(boards):
            break;

    for row in boards[winning_boards[-1]]:
        for number in row:
            if number not in drawed_numbers:
                unmarked_score += int(number);

    Buddy().outputAnswer(
        "Unmarked score: " + str(unmarked_score),
        "Answer is: " + str(unmarked_score * int(drawed_numbers[-1])),
    );

## 19 days until christmas 🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄🎅🏻🎄
day_four();