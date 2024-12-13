# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import re

P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def split_buttons(line_str:str, delim = "+"):
    match = re.search(r"X\%s(\d+), Y\%s(\d+)" % (delim, delim), line_str)[0].split(", ")
    return int(match[0].split(delim)[1]), int(match[1].split(delim)[1])


def part1(input):
    total = 0
    for machine in input:

        lines = machine.split("\n")
        ax, ay = split_buttons(lines[0])
        bx, by = split_buttons(lines[1])
        x_val, y_val = split_buttons(lines[2], "=")

        y = (y_val * ax - x_val * ay) / (ax * by - ay * bx)
        x = (x_val - bx * y) / ax

        if int(x) == x and int(y) == y:
            if P1_DEBUG: print(f"Pressing the A button {int(x)} times, and the B button {int(y)} times results in ending up at {(x_val, y_val)}")
            total += 3 * x + y
        else:
            if P1_DEBUG: print(f"\t Cannot reach {(x_val, y_val)} on this machine")

    return int(total)


def part2(input):
    total = 0
    for machine in input:

        lines = machine.split("\n")
        ax, ay = split_buttons(lines[0])
        bx, by = split_buttons(lines[1])
        x_val, y_val = split_buttons(lines[2], "=")
        x_val += 10000000000000
        y_val += 10000000000000

        y = (y_val * ax - x_val * ay) / (ax * by - ay * bx)
        x = (x_val - bx * y) / ax

        if int(x) == x and int(y) == y:
            if P1_DEBUG: print(f"Pressing the A button {int(x)} times, and the B button {int(y)} times results in ending up at {(x_val, y_val)}")
            total += 3 * x + y
        else:
            if P1_DEBUG: print(f"\t Cannot reach {(x_val, y_val)} on this machine")

    return int(total)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
