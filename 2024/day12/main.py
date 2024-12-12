# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = False # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Do Floodfill/DFS to calculate the perimeter and area
def calculate_perimeter_and_area(grid: list[list[str]], row_index:int, column_index:int, letter: str, visited:list[list[any]]):
    stack = [(row_index, column_index)]
    visited[row_index][column_index] = True
    perimeter = 0
    area = 0
    corners = 0 # TODO: Added for PT2

    while stack:
        c_row, c_col = stack.pop()
        area += 1

        # check the directional neighbours for perimeter boundaries
        for d_row, d_col in directions:
            new_row, new_col = c_row + d_row, c_col + d_col

            if not aoc_common.is_in_bounds_of_grid(grid, (new_row, new_col)) or grid[new_row][new_col] != letter:
                perimeter += 1

            elif not visited[new_row][new_col] and grid[new_row][new_col] == letter:
                visited[new_row][new_col] = True
                stack.append((new_row,new_col))

    return perimeter, area, corners


def find_regions(grid: list[list[str]]):
    visited = [[False] * len(grid[0]) for i in range(len(grid))]
    letter_regions = {}

    for ri, row in enumerate(grid):
        for ci, col in enumerate(grid):
            if not visited[ri][ci]:
                letter = grid[ri][ci]
                perimeter, area, corners = calculate_perimeter_and_area(grid, ri, ci, letter, visited)

                if letter not in letter_regions:
                    letter_regions[letter] = []
                letter_regions[letter].append((perimeter, area, corners))

    return letter_regions


def part1(input):
    return True


def part2(input):
    regions = find_regions(input)
    price = 0

    for letter, region in regions.items():
        for i, (perimeter, area, corners) in enumerate(region, 1):
            price += area * corners
            if P2_DEBUG: print(f"A region {letter} plants with price {area} * {corners} = {area * corners}")
            # print()

    return price


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    print("p2")
    print ()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
