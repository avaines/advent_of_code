# pylint: disable-all
# Import AOC Common
import os
import sys
import re
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample2.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    memory = ''.join(input)
    total=0

    multiply_matches = re.findall("mul\((\d+),(\d+)\)", memory)

    for match in multiply_matches:
        total+=int(match[0])*int(match[1])

    return total


def part2(input):
    memory = ''.join(input)
    total=0

    while True:
        start_index = memory.find("don't()")
        end_index = memory.find("do()", start_index)

        if start_index != -1 and end_index != -1:
            memory = memory[:start_index] + memory[end_index + len("do()"):]
        else:
            # No more matches
            break

        multiply_matches = (re.findall("mul\((\d+),(\d+)\)", memory))

    total=0
    for match in multiply_matches:
        total+=int(match[0])*int(match[1])

    return total


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part 1:", part_1 )
    print("Part 2:", part_2 )
