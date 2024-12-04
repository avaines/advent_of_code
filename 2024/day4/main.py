# pylint: disable-all
# Import AOC Common
import os
import sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from collections import Counter

P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    match_list = aoc_algorithms.grid_word_search(input, "XMAS")

    return len(match_list)


def part2(input):
    match_list = aoc_algorithms.grid_word_search(input, "MAS", vertical=False, horizontal=False)

    all_coords = [coord for match in match_list for coord in match[1:-1]] # Ignore the 1st and last items, because overlaps should form an X not an angle

    coord_counts = Counter(all_coords) # Counter tallies occurrences of words like ({'blue': 3, 'red': 2, 'green': 1})

    overlaps = {coord: count for coord, count in coord_counts.items() if count > 1}

    return len(overlaps)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part 1:", part_1 )
    print("Part 2:", part_2 )
