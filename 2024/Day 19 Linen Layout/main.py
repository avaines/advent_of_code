# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from collections import defaultdict


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def is_valid_design(design, towels, index=0):
    if index == len(design):
        return True

    for towel in towels:
        next_index = index + len(towel)
        if next_index <= len(design) and design[index:next_index] == towel:
            if is_valid_design(design, towels, next_index):
                return True

    return False


def part1(towels, designs):
    count = 0
    for design in designs:
        if is_valid_design(design, towels):
            if P1_DEBUG: print(f"{design} is valid")
            count += 1

    return count


cache = defaultdict(int)
def count_valid_designs(design, towels, index=0):
    if index == len(design):
        return 1

    if cache[index] > 0:
        return cache[index]

    matches = 0
    for towel in towels:
        next_index = index + len(towel)
        if next_index <= len(design) and design[index:next_index] == towel:
            matches += count_valid_designs(design, towels, next_index)

    cache[index] = matches
    return matches


def part2(towels, designs):

    total = 0
    for design in designs:
        cache.clear()
        total += count_valid_designs(design, towels)

    return total


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    towels = parsed_input[0].split(", ")
    designs= parsed_input[1].split("\n")[:-1]

    start_time_part1 = time.time()
    part_1 = part1(towels, designs)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(towels, designs)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
