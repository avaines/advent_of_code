"""
Day X: Title
"""
import itertools
from os import curdir

def part1(puzzle_input, debug):
    max_joltage = max(puzzle_input) + 3
    puzzle_input.append(max_joltage)
    diff_1_jolts = 0
    diff_2_jolts = 0
    diff_3_jolts = 0

    cur_adapter_joltage = 0

    while cur_adapter_joltage != max(puzzle_input):
        next_adapter_joltage = min([j for j in puzzle_input if j > cur_adapter_joltage])
        if debug: print("current joltage:", cur_adapter_joltage, "next adapter has a joltage of:", next_adapter_joltage)

        if next_adapter_joltage - cur_adapter_joltage == 1: diff_1_jolts +=1
        elif next_adapter_joltage - cur_adapter_joltage == 2: diff_2_jolts +=1
        elif next_adapter_joltage - cur_adapter_joltage == 3: diff_3_jolts +=1

        cur_adapter_joltage = next_adapter_joltage

    return diff_1_jolts * diff_3_jolts


def part2(puzzle_input, debug):
    # process puzzle_input
    # implement algorithm i dont know about
    # ???
    return "profit"


with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

puzzle_input_ints = [ int(x) for x in puzzle_input ]

p1 = part1(puzzle_input_ints, False)
p2 = part2(puzzle_input_ints, True)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )