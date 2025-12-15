# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_intcode_computer #, aoc_algorithms, aoc_grid_tools
from copy import deepcopy


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    input_values = [1]  # ship's air conditioner unit
    COMPUTER = aoc_intcode_computer.initcode_computer(program=input, input_values=input_values)
    COMPUTER.run()

    return COMPUTER.output_values[-1]


def part2(input):
    input_values = [5]  # ship's thermal radiator controller
    COMPUTER = aoc_intcode_computer.initcode_computer(program=input, input_values=input_values)
    COMPUTER.run()

    return COMPUTER.output_values[-1]

if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = [int(x) for x in parsed_input[0].split(",")]

    start_time_part1 = time.time()
    part_1 = part1(deepcopy(parsed_input))
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(deepcopy(parsed_input))
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
