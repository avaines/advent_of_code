# pylint: disable-all
# Import AOC Common
from itertools import count
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms #, aoc_grid_tools


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def count_paths(graph, start, end, memo=None):
    '''
    https://www.reddit.com/r/leetcode/comments/1flttfk/graph_dfs_memoization/
    https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
    '''

    # Can't use memo={} as default arg as defaults persist between calls. Could move to a nested fn?
    if memo is None:
        memo = {}

    if start == end:
        return 1

    if start in memo:
        return memo[start]

    # Handle nodes not in graph ('out' node throws a wobbler otherwise)
    if start not in graph:
        memo[start] = 0
        return 0

    total = sum([count_paths(graph, neighbor, end, memo) for neighbor in graph[start]])
    memo[start] = total
    return total


def part1(input):
    # num_paths = count_graph_paths(graph=input, start="you", end="out") # After a rewrite for p2 back ported p1 to that mechanism
    num_paths = count_paths(input, 'you', 'out')
    if P1_DEBUG: print("Part 1 done")
    return num_paths


def part2(input):
    num_paths_svr_fft = count_paths(input, 'svr', 'fft')
    num_paths_fft_dac = count_paths(input, 'fft', 'dac')
    num_paths_dac_out = count_paths(input, 'dac', 'out')

    if P2_DEBUG: print("Part 2 done")
    return (num_paths_svr_fft * num_paths_fft_dac * num_paths_dac_out)


def unpack_input(input):
    parsed_input = {}
    for line in input:
        a,*b = line.split(' ')
        parsed_input[a[:-1]] = b

    return parsed_input


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = unpack_input(parsed_input)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
