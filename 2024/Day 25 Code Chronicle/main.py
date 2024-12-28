# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from itertools import combinations


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def pin_counts(object):
    pins = [-1,-1,-1,-1,-1]

    for ri, row in enumerate(object):
        for ci, col in enumerate(row):
            if col == "#":
                pins[ci] += 1

    return pins


def part1(input):
    locks = []
    keys = []

    for object in input:
        if object[0]=="#####":
            locks.append(pin_counts(object))
        elif object[-1]=="#####":
            keys.append(pin_counts(object))

    matches = 0
    for lock in locks:
        for key in keys:
            if all(k+l<=5 for k,l in zip(key,lock)):
                if P1_DEBUG: print(f"Lock {lock} and key {key} Match!")
                matches +=1
            else:
                if P1_DEBUG: print(f"Lock {lock} and key {key} overlap")

    return matches


# def part2(input):
#     if P2_DEBUG: print(f"Doing Part 2 things")
#     return "part 2 answer"


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = [x.split('\n') for x in parsed_input]
    del parsed_input[-1][-1] # very lazy handling

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    # start_time_part2 = time.time()
    # part_2 = part2(parsed_input)
    # end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    # print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
