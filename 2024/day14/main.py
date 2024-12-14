# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import re


P1_DEBUG = False
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

WIDTH = 101 if USE_REAL_DATA else 11
HEIGHT = 103 if USE_REAL_DATA else 7


class bathroom:
    def __init__(self):
        self.grid = aoc_algorithms.generate_grid(WIDTH, HEIGHT, ".")
        self.bots_present_grid = aoc_algorithms.generate_grid(WIDTH, HEIGHT, ".")
        self.robots = {}


    def init_robot(self, id, current_pos, velocity):
        # p=(x,y) x represents the number of tiles the robot is from the left wall and y
        # v=(x,y) Positive x means the robot is moving to the right, and positive y means the robot is moving down.
        self.robots[id] = {"p": current_pos, "v": velocity}

        if self.grid[current_pos[1]][current_pos[0]] == ".":
            self.grid[current_pos[1]][current_pos[0]] = 1
        else:
            self.grid[current_pos[1]][current_pos[0]] +=1



    def move_robots(self):
        self.grid = aoc_algorithms.generate_grid(WIDTH, HEIGHT, ".")
        self.bots_present_grid = aoc_algorithms.generate_grid(WIDTH, HEIGHT, ".")

        for robot in self.robots:
            r_pos = self.robots[robot]['p']
            r_vel = self.robots[robot]['v']
            n_pos_x = (r_pos[0] + r_vel[0]) % WIDTH
            n_pos_y = (r_pos[1] + r_vel[1]) % HEIGHT
            self.robots[robot]['p'] = (n_pos_x, n_pos_y)

            self.bots_present_grid[n_pos_y][n_pos_x]="#"
            if self.grid[n_pos_y][n_pos_x] == ".":
                self.grid[n_pos_y][n_pos_x] = 1
            else:
                self.grid[n_pos_y][n_pos_x] +=1


    def draw(self):
        aoc_common.draw_grid_to_console(self.grid, 1)


    def get_area_safety_factors(self, grid, top_left, bottom_right):
        x1, y1 = top_left
        x2, y2 = bottom_right
        safety_factor = 0

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                value = grid[y][x]
                if isinstance(value, int):
                    safety_factor += value

        return safety_factor


    def get_quadrant_safety_factors(self):
        grid = aoc_algorithms.generate_grid(WIDTH, HEIGHT, ".")
        for robot in self.robots:
            robot_pos = self.robots[robot]['p']
            if grid[robot_pos[1]][robot_pos[0]] == ".":
                grid[robot_pos[1]][robot_pos[0]] = 1
            else:
                grid[robot_pos[1]][robot_pos[0]] +=1

        # Q1
        q1_top_left = (0, 0)
        q1_bottom_right = (WIDTH//2-1, HEIGHT//2-1)
        q1_safety_factor = self.get_area_safety_factors(grid, q1_top_left, q1_bottom_right)

        # Q2
        q2_top_left = (WIDTH//2, 0)
        q2_bottom_right = (WIDTH-1, HEIGHT//2-1)
        q2_safety_factor = self.get_area_safety_factors(grid, q2_top_left, q2_bottom_right)

        # Q3
        q3_top_left = (0, HEIGHT//2+1)
        q3_bottom_right = (WIDTH//2-1, HEIGHT-1)
        q3_safety_factor = self.get_area_safety_factors(grid, q3_top_left, q3_bottom_right)

        # Q4
        q4_top_left = (WIDTH//2+1, HEIGHT//2+1)
        q4_bottom_right = (WIDTH-1, HEIGHT-1)
        q4_safety_factor = self.get_area_safety_factors(grid, q4_top_left, q4_bottom_right)

        return q1_safety_factor, q2_safety_factor, q3_safety_factor, q4_safety_factor



def part1(input):
    ticks=100
    p1_bathroom = bathroom()

    for robot_id, robot_instructions in enumerate(input):
        match = re.findall(r'[pv]=(-?\d+),(-?\d+)', robot_instructions)
        positions = tuple(map(int, match[0]))
        velocities = tuple(map(int, match[1]))

        p1_bathroom.init_robot(robot_id+1, positions, velocities)

    if P1_DEBUG:
        p1_bathroom.draw()
        print("Initial State")

    for tick in range(0,ticks):
        p1_bathroom.move_robots()

        if P1_DEBUG:
            p1_bathroom.draw()
            print(f"After {tick+1} seconds")

    return aoc_common.product(p1_bathroom.get_quadrant_safety_factors())


def part2(input):
    ticks=10000
    p2_bathroom = bathroom()

    for robot_id, robot_instructions in enumerate(input):
        match = re.findall(r'[pv]=(-?\d+),(-?\d+)', robot_instructions)
        positions = tuple(map(int, match[0]))
        velocities = tuple(map(int, match[1]))

        p2_bathroom.init_robot(robot_id+1, positions, velocities)

    if P2_DEBUG:
        p2_bathroom.draw()
        print("Initial State")


    lowest_danger_rating = float('inf')

    for tick in range(1,ticks):
        p2_bathroom.move_robots()

        # # Assuming this is something to do with the danger rating?
        # this_danger_rating = aoc_common.product(p2_bathroom.get_quadrant_safety_factors())
        # if this_danger_rating < lowest_danger_rating:
        #     lowest_danger_rating = this_danger_rating
        #     if P2_DEBUG:
        #         p2_bathroom.draw()
        #         print(f"After {tick} seconds")

        # # Lets assume 1/3 of the robots would be in a single quadrant? Noop
        # quadrants = p2_bathroom.get_quadrant_safety_factors()
        # for bots_in_quad in quadrants:
        #     if bots_in_quad > len(input)/3:
        #         if P2_DEBUG:
        #             p2_bathroom.draw()
        #             print(f"After {tick+1} seconds")

        # # Can I just scum the solution, assuming the bottom row of the tree would be sufficiently wide?
        for row in p2_bathroom.bots_present_grid:
            if "#"*10 in ''.join(row):
                if P2_DEBUG:
                    p2_bathroom.draw()
                    print(f"After {tick} seconds")
                return tick


    return tick


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
