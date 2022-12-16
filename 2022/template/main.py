
# Import AOC Common
import sys
sys.path.append("../shared")
import aoc_common

import os

INPUT_DEBUG = True
P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = False # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    if INPUT_DEBUG: print("Parsing the input")
    return input

def part1(input):
    if P1_DEBUG: print("Doing Part 1 things")
    return "part 1 answer"

def part2(input):
    if P2_DEBUG: print("Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )