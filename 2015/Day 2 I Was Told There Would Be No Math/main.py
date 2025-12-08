# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools
import math


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def calc_present_sq_ft(present_dimensions):
    pds = [int(i) for i in present_dimensions.split("x")]
    side_area = [
        (pds[0] * pds[1]),
        (pds[1] * pds[2]),
        (pds[2] * pds[0])
    ]

    surface_area = [2 * i for i in side_area]

    total_sq_ft = sum(surface_area) + min(side_area)

    if P1_DEBUG: print(f"For a present of {present_dimensions}, it has a total of {sum(surface_area)} square foot, plus {min(surface_area)} slack for {total_sq_ft}")
    return total_sq_ft


def calc_ribbon_length(present_dimensions):
    pds = [int(i) for i in present_dimensions.split("x")]

    present_volume = math.prod(pds) #bow

    bow_length = min(pds) *2
    pds.remove(min(pds))
    bow_length += min(pds) *2

    if P2_DEBUG: print(f"For a present of {present_dimensions}, it has a bow length of {bow_length} feet, plus {present_volume} feet for a bow for {bow_length + present_volume}")
    return bow_length + present_volume


def part1(input):
    total_sq_ft = 0

    for present in input:
        present_sq_ft = calc_present_sq_ft(present)
        total_sq_ft += present_sq_ft

    return total_sq_ft


def part2(input):
    total_ribbon_length = 0

    for present in input:
        present_ribbon_length = calc_ribbon_length(present)
        total_ribbon_length += present_ribbon_length

    return total_ribbon_length


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
