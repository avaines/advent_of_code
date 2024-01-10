
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False
if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data(2023, 15)

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def calculate_hash(sequence):
    value = 0

    for char in [*sequence]:
        value += ord(char)
        value = value * 17
        value = value % 256

    return value

def part1(input):
    sequence = []

    for i in input:
        sequence.append(calculate_hash(i))

    return sum(sequence)


def part2(input):
    if P2_DEBUG: print(f"Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = parsed_input[0].split(",")

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
