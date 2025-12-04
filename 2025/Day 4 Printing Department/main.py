# pylint: disable-all
# Import AOC Common
import os
import sys
import time
from copy import deepcopy
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = False
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def processGrid(grid):
    accessableRollsOfPaper = 0
    accessableRollsOfPaperPositions = []
    for ri,row in enumerate(grid):
        for ci, column in enumerate(row):
            # if current pos is a a roll of paper, get all its neighbours
            if column == "@":
                x = aoc_algorithms.get_all_grid_neighbours(ri, ci, grid, diagonals=True)

                # count em, if theres less than 4 rolls of paper its accessible
                rollsOfPaper = x["values"].count("@")
                if rollsOfPaper<4:
                    if P1_DEBUG: print(f"{ri},{ci} has {rollsOfPaper} rolls of paper nearby")
                    accessableRollsOfPaper += 1
                    accessableRollsOfPaperPositions.append((ri,ci))

    for pos in accessableRollsOfPaperPositions:
        grid[pos[0]][pos[1]] = "."

    return grid, accessableRollsOfPaper


def part1(input):
    grid, accessableRollsOfPaper = processGrid(input)
    if P1_DEBUG: aoc_common.draw_grid_to_console(grid)
    return accessableRollsOfPaper


def part2(input):
    accessableRollsOfPaper = -1
    totalRollsOfPaperRemoved = 0

    while accessableRollsOfPaper !=0:
        input, accessableRollsOfPaper = processGrid(input)
        totalRollsOfPaperRemoved += accessableRollsOfPaper
        if P2_DEBUG: aoc_common.draw_grid_to_console(input, headerText=f"Total rolls of paper removed so far: {totalRollsOfPaperRemoved}", delay=0.5)

    return totalRollsOfPaperRemoved


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(deepcopy(parsed_input))
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(deepcopy(parsed_input))
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
