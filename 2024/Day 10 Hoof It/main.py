# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from collections import deque

P1_DEBUG = False
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample2.txt" % os.path.dirname(os.path.realpath(__file__))


def ordnance_survey(topo:list[list[int]], cur_location:list[int], path):
    directions = [
        (-1,0),
        (1,0),
        (0,1),
        (0,-1),
    ]

    if topo[cur_location[0]][cur_location[1]] == 9:
        return [path]
    else:
        paths = []
        for d in directions:
            new_location = (cur_location[0] + d[0], cur_location[1] + d[1])
            if 0 <= new_location[0] < len(topo) and 0 <= new_location[1] < len(topo[0]):
                if topo[new_location[0]][new_location[1]] == topo[cur_location[0]][cur_location[1]] + 1:
                    if P1_DEBUG: print(f"{(new_location[0],new_location[1])}: {topo[new_location[0]][new_location[1]]} looks like the next step")
                    paths += ordnance_survey(topo, new_location, path +[new_location])

        return paths


def part1(input):
    trailheads = []
    for ri, r in enumerate(input):
        for ci, c in enumerate(r):
            if input[ri][ci] == 0:
                trailheads.append((ri,ci))

    if P1_DEBUG: print(f"Found {len(trailheads)} trailheads")

    all_routes = []
    for trailhead in trailheads:
        all_routes.append(ordnance_survey(input, trailhead, []))

    p1_trailhead_score = 0
    p2_trailhead_score = 0

    for route in all_routes:
        p2_trailhead_score += len(route)
        unique_routes = set()
        for r in route:
            unique_routes.add(r[-1])

        p1_trailhead_score += len(unique_routes)

    return p1_trailhead_score, p2_trailhead_score


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = aoc_common.convert_list_of_lists_to_ints(parsed_input)

    start_time_part1 = time.time()
    part_1, part_2 = part1(parsed_input)
    end_time_part1 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2}")
