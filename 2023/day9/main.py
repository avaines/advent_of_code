
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from itertools import pairwise

P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False
if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data(2023, 9)

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def evaluate_row(row, part2=False):
    if set(row) == {0}:
        return 0

    next_row = [b - a for a, b in pairwise(row)]
    result = evaluate_row(next_row, part2)

    if part2:
        return row[0] - result
    else:
        return row[-1] + result


def part1(input):
    evaluated_rows = []
    for row in input:
        evaluated_rows.append(evaluate_row(row))

    return sum(evaluated_rows)


def part2(input):
    evaluated_rows = []
    for row in input:
        evaluated_rows.append(evaluate_row(row, True))

    return sum(evaluated_rows)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_rows = []

    for row in parsed_input:
        parsed_rows.append([int(v) for v in row.split(" ")])

    part_1 = part1(parsed_rows)
    part_2 = part2(parsed_rows)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
