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


def part1(presents, bins):
    valid_bins = []

    for bin in bins:
        # if P1_DEBUG: print(f"Bin: {bin}")
        bin_width, bin_length = map(int, bin[0].rstrip(':').split('x'))
        present_counts = sum(int(x) for x in bin[1:])
        total_capacity = (bin_width // 3) * (bin_length // 3)

        if present_counts <= total_capacity:
            if P1_DEBUG: print(f"Valid bin found: {bin} with capacity {total_capacity} for {present_counts} presents")
            valid_bins.append(bin)

    return len(valid_bins)


def part2(presents, bins):
    if P2_DEBUG: print(f"Doing Part 2 things")
    return "part 2 answer"


def unpack(input):
    # this one is a bit gross.
    presents = {}
    bins = []
    for line in input:
        if 'x' in line:
            # This is a bin, not a present, comes in a single line
            bins = [x.split(' ') for x in line.split('\n')]
            if bins[-1] == ['']:
                bins = bins[0:-1]
            pass
        else:
            # This is a present
            present = [list(x) for x in line.split('\n')]
            id = int(''.join(present[0][0:-1]))
            presents[id] = present[1:]

    return presents, bins

if __name__ == '__main__':
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    presents, bins = unpack(parsed_input)

    start_time_part1 = time.time()
    part_1 = part1(presents, bins)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(presents, bins)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
