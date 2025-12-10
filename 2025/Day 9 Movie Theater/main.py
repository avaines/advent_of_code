# pylint: disable-all
# Import AOC Common
import os
import string
import sys
import time

from shapely import area
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools
from shapely.geometry import Polygon


P1_DEBUG = False
P2_DEBUG = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    max_area = 0
    # for all the tiles find pairs

    # take a tile, take all the other tiles. then work out the diff in the x and the y and multipy them to gether for the aread
    # Thank you Sean for the OBO's
    for i in input:
        for j in input:
            x_diff = abs(i[0] - j[0]) +1
            y_diff = abs(i[1] - j[1]) +1
            max_area = max(max_area, x_diff * y_diff)
            if P1_DEBUG: print(f"Tile {i} to Tile {j} = Area {max_area}")

    return max_area


# This is something to do with AABB Axis Aligned Bounding Boxes
# Kinda cheated a little on this one via tihs reddit thread https://www.reddit.com/r/adventofcode/comments/1pi3hff/2025_day_9_part_2_a_simple_method_spoiler/ 
# https://kishimotostudios.com/articles/aabb_collision/ was the way I understood it
# https://stackoverflow.com/questions/25231241/detecting-intersection-of-arbitrarily-rotated-text-in-matplotlib
def part2(input):
    polygon_coords = [(x[0], x[1]) for x in input] # https://shapely.readthedocs.io/en/stable/reference/shapely.Polygon.html
    max_area = 0

    # Creates a polygon representing the valid red/green area
    red_green_area = Polygon(polygon_coords)

    # Try all possible pairs of points to form rectangles like P1
    for i in input:
        for j in input:
            # Create a rectangle using points i and j as opposite corners, again like p1
            rectangle = Polygon([(i[0], i[1]), (i[0], j[1]), (j[0], j[1]), (j[0], i[1])])

            # Check if this rectangle is FULLY contained within the red/green area
            if red_green_area.contains(rectangle):
                # Figure out the area like in P1
                x_diff = abs(i[0] - j[0]) +1
                y_diff = abs(i[1] - j[1]) +1
                max_area = max(max_area, x_diff * y_diff)
                if P2_DEBUG: print(f"Rectangle {rectangle} is contained in Red/Green area with area {max_area}")

    return max_area


def calc_area(x1, y1, x2, y2):
    width = abs(int(x2) - int(x1)) + 1
    height = abs(int(y2) - int(y1)) + 1
    return width * height

def create_rectangle(x1, y1, x2, y2):
    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])



if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = [list(map(int, line.split(','))) for line in parsed_input]

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
