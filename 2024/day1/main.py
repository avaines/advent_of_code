# pylint: disable-all
# Import AOC Common
import os
import sys
sys.path.append("../")
from shared import aoc_common


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(left,right):
    diffs=[]
    for i in range(len(left)):
        diffs.append(abs(left[i]-right[i]))

    return sum(diffs)


def part2(left,right):
    similarity_scores = []
    for n in left:
        similarity_scores.append(n*right.count(n))

    return sum(similarity_scores)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    left=[int(x.split()[0]) for x in parsed_input]
    right=[int(x.split()[1]) for x in parsed_input]

    part_1 = part1(sorted(left),sorted(right))
    part_2 = part2(left, right)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
