# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools
import re

P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def is_nice(string):
    if len(re.findall(r'[aeiou]', string)) < 3: return False
    if not bool(re.search(r'(\w)\1', string)): return False
    if bool(re.search(r'(ab|cd|pq|xy)', string)): return False
    return True


def is_nice_v2(string):
    if not bool(re.search(r'(\w\w).*\1', string)): return False
    if not bool(re.search(r'(\w)\w\1', string)): return False
    return True


def part1(input):
    nice_strings = []
    for string in input:
        if is_nice(string):
            if P1_DEBUG: print(f"{string}, is nice")
            nice_strings.append(string)
        else:
            if P1_DEBUG: print(f"{string}, is naughty")

    return len(nice_strings)


def part2(input):
    nice_strings = []
    for string in input:
        if is_nice_v2(string):
            if P2_DEBUG: print(f"{string}, is nice")
            nice_strings.append(string)
        else:
            if P2_DEBUG: print(f"{string}, is naughty")

    return len(nice_strings)


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
