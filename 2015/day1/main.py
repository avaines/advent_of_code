
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def part1(input):
    target_floor = 0 # ground floor
    for char in [*input[0]]:
        match char:
            case "(":
                if P1_DEBUG: print("Going UP 1 floor")
                target_floor += 1
            case ")":
                if P1_DEBUG: print("Going DOWN 1 floor")
                target_floor -= 1

    return target_floor

def part2(input):
    target_floor = 0 # ground floor
    for index, char in enumerate([*input[0]]):
        match char:
            case "(":
                if P1_DEBUG: print("Going UP 1 floor")
                target_floor += 1
            case ")":
                if P1_DEBUG: print("Going DOWN 1 floor")
                target_floor -= 1

        if target_floor == -1:
            if P1_DEBUG: print("Entering Basement...")
            return index+1


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )