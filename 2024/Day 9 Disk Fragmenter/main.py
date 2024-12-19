# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = False
P2_DEBUG = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def parse_blocks(disk_map):
    blocks = []
    file_id = 0

    for i, block in enumerate(disk_map):
        if i % 2 == 0:
            blocks += block * [file_id]
        else:
            blocks += block * ["."]
            file_id +=1
    print()
    return blocks


def is_sorted(disk_map):
    first_space_index = disk_map.index(".")
    remaining_map = disk_map[first_space_index:]
    if all(x == "." for x in remaining_map):
        return True
    else:
        return False


def defrag_step(disk_map):
    for move_candidate_index in range(len(disk_map)-1,0,-1):
        if disk_map[move_candidate_index] != ".":
            for space_index in range(0,len(disk_map)-1):
                if disk_map[space_index] == ".":
                    disk_map[space_index] = disk_map[move_candidate_index]
                    disk_map[move_candidate_index] = "."
                    return disk_map


def part1(input):
    parsed_disk_map = parse_blocks(input)

    if P1_DEBUG: aoc_common.draw_grid_to_console([''.join(str(i) for i in parsed_disk_map)])

    while not is_sorted(parsed_disk_map):
        parsed_disk_map = defrag_step(parsed_disk_map)
        if P1_DEBUG: aoc_common.draw_grid_to_console([''.join(str(i) for i in parsed_disk_map)])

    checksum = 0
    for i, block in enumerate(parsed_disk_map):
        if block !=".":
            checksum += i * block
            if P1_DEBUG: print(f"{i} * {block} = {i * block}")

    return checksum

def find_group_indexes(lst, character):
    groups = []
    start = None
    for i, val in enumerate(lst):
        if val == character:
            if start is None:
                start = i
        else:
            if start is not None:
                groups.append((start, i - 1))
                start = None

    if start is not None:
        groups.append((start, len(lst) - 1))

    return groups


def part2(input):
    parsed_disk_map = parse_blocks(input)

    if P2_DEBUG: aoc_common.draw_grid_to_console([''.join(str(i) for i in parsed_disk_map)])

    unique_file_ids = list(set( [i for i in parsed_disk_map if i != "."] ))
    unique_file_ids = list(reversed(unique_file_ids))

    for unique_file in unique_file_ids:
        spaces = find_group_indexes(parsed_disk_map, ".")
        file_block = find_group_indexes(parsed_disk_map, unique_file)[0]
        file_block_range = list(range(file_block[0],file_block[1]+1))

        if P2_DEBUG: print(f"file with id {unique_file} is {len(file_block_range)} blocks long")

        for space in spaces:
            if len(range(space[0],space[1]+1)) >= len(file_block_range) and space[0] < file_block_range[0]: #If there is a space and the space is left most of where it already starts
                space_range = list(range(space[0],space[1]+1))
                if P2_DEBUG: print(f"Moving the {unique_file}'s at {file_block} to {space}")
                for i, file_block_idx in enumerate(file_block_range):
                        parsed_disk_map[space_range[i]] = unique_file
                        parsed_disk_map[file_block_idx] = "."

                if P2_DEBUG: aoc_common.draw_grid_to_console([''.join(str(i) for i in parsed_disk_map)], clear=False)
                break

    checksum = 0
    for i, block in enumerate(parsed_disk_map):
        if block !=".":
            checksum += i * block
            if P2_DEBUG: print(f"{i} * {block} = {i * block}")

    return checksum


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    parsed_input= list(map(int, list(parsed_input[0])))

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
