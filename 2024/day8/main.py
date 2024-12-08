# pylint: disable-all
# Import AOC Common
import os
import sys
import time
import math
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from collections import defaultdict
from itertools import combinations

P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    antennae = defaultdict(list)
    for x, row in enumerate(input):
        for y, char in enumerate(row):
            if char != ".":
                antennae[char].append((x,y))
    
    antinodes = set()
    for group in antennae.values():
        for p1, p2 in combinations(group, 2):
            # The pair should be x *2 -the other one in the pair, same for the y axis to find out where the other ones needs to go.
            antinode_pair = [
                (p2[0] * 2 - p1[0], p2[1] * 2 - p1[1]),
                (p1[0] * 2 - p2[0], p1[1] * 2 - p2[1]),
            ]

            for antinode in antinode_pair:
                # Check this pair is in bounds
                if 0 <= antinode[0] < len(input) and 0 <= antinode[1] < len(input[0]):
                    antinodes.add(antinode)
                else:
                    print()

    return len(antinodes)


def part2(input):
    antennae = defaultdict(list)
    for x, row in enumerate(input):
        for y, char in enumerate(row):
            if char != ".":
                antennae[char].append((x,y))
    
    antinodes = set()
    for group in antennae.values():
        for p1, p2 in combinations(group, 2):
            # it said 'exactly in line' so i assume theres a division issue somwehere
            # Thanks stack overflow
            greatest_common_demnominator = math.gcd(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
            move_distance = (p2[0] - p1[0])//greatest_common_demnominator, (p2[1] - p1[1])//greatest_common_demnominator

            for silly_big_area in (range(0,1000), range(-1, -1000, -1)):
                for x in silly_big_area:
                    antinode = (p1[0] + x * move_distance[0], p1[1] + x * move_distance[1])
                    
                    # Check this pair is in bounds like part 1
                    if 0 <= antinode[0] < len(input) and 0 <= antinode[1] < len(input[0]):
                        antinodes.add(antinode)

    return len(antinodes)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    
    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
