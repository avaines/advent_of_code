# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


# (x(horz), y(vert))
def move_direction(start_location, direction):
    match direction:
        case ">":
            new_location = (start_location[0] +1, start_location[1])
        case "<":
            new_location = (start_location[0] -1, start_location[1])
        case "^":
            new_location = (start_location[0], start_location[1] +1)
        case "v":
            new_location = (start_location[0], start_location[1] -1)

    return new_location


def part1(input):
    current_location = (0,0)
    locations_visited = [current_location]

    for instruction in [*input[0]]:
        current_location = move_direction(current_location, instruction)
        locations_visited.append(current_location)

    unique_locations_visited = list(set(locations_visited))
    return len(unique_locations_visited)


def part2(input):
    s_current_location = (0,0)
    rs_current_location = (0,0)

    s_locations_visited = [s_current_location]
    rs_locations_visited = [rs_current_location]

    for index, instruction in enumerate([*input[0]]):
        if index % 2 == 0:
            s_current_location = move_direction(s_current_location, instruction)
            s_locations_visited.append(s_current_location)
        else:
            rs_current_location = move_direction(rs_current_location, instruction)
            rs_locations_visited.append(rs_current_location)

    unique_locations_visited = list(set(s_locations_visited + rs_locations_visited))

    return len(unique_locations_visited)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
