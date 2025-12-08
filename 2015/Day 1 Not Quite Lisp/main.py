# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
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

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
