"""
task summary/notes
"""

import fileinput
import collections


def part1(puzzle_input):
    for entry in puzzle_input:
        for entry_n in puzzle_input:
            # print(entry, "+", entry_n, "=", int(entry)+int(entry_n))
            if int(entry) + int(entry_n) == 2020:
                return int(entry), int(entry_n)

    return 0


def part2(input):
    for entry in puzzle_input:
        for entry_n in puzzle_input:
            for entry_nn in puzzle_input:
                # print(entry, "+", entry_n, "=", int(entry)+int(entry_n))
                if int(entry) + int(entry_n) + int(entry_nn) == 2020:
                    return int(entry), int(entry_n), int(entry_nn)


    return 0


# puzzle_input = list(fileinput.input('sample1.txt'))
with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input)
print( p1[0] * p1[1] )

p2 = part2(puzzle_input)
print( p2[0] * p2[1] * p2[2] )