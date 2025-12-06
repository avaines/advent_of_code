# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from itertools import zip_longest # regula zip stops at the shortest sting

P1_DEBUG = False
P2_DEBUG = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    running_total = 0

    for problem in input:
        values = map(int, problem[:-1])
        op = problem[-1].strip()
        this_problem_solution = aoc_common.product(values) if op == '*' else sum(values)
        if P1_DEBUG: print(f"Problem: {problem} => {this_problem_solution}")
        running_total += this_problem_solution

    return running_total


def part2(input):
    running_total = 0

    # the explanation does this backwards, so ive obviously done this wrong
    for problem_id in range(len(input)):
        problem = input[len(input) -1 - problem_id]
        this_problem = ""
        transposed = list(zip_longest(*problem[:-1], fillvalue=' ')) # pad the shorter string first so all same length with zip_longest

        for si, sum in enumerate(reversed(transposed)):
            this_problem += ''.join(sum)
            if si < len(transposed) -1:
                this_problem += problem[-1]

        this_problem_solution = eval(this_problem)
        if P2_DEBUG: print(f"Problem: {this_problem} => {this_problem_solution}")
        running_total += this_problem_solution

    return running_total


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_preformatted_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = aoc_common.rotate_grid_90_anticlockwise(parsed_input)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
