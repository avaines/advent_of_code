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
SAMPLE_FILENAME = "%s/sample2.txt" % os.path.dirname(os.path.realpath(__file__))

DIRECTIONS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}

class warehouse:

    def __init__(self, initial_grid):
        self.grid = initial_grid
        self.robot_position = next((ri, ci) for ri, row in enumerate(self.grid) for ci, cell in enumerate(row) if cell == "@")


    def calculate_gps(self):
        gps_score=0

        for ri, row in enumerate(self.grid):
            for ci, c in enumerate(row):
                if self.grid[ri][ci] == "O":
                    gps_score += 100 * ri + ci

        return gps_score


    def update_position(self, old_pos, new_pos):
        char = self.grid[old_pos[0]][old_pos[1]]
        self.grid[old_pos[0]][old_pos[1]] = "."
        self.grid[new_pos[0]][new_pos[1]] = char
        if char == "@": self.robot_position = new_pos


    def move_target(self, instruction, position):
        new_position = (position[0] + DIRECTIONS[instruction][0], position[1] + DIRECTIONS[instruction][1])

        while self.grid[new_position[0]][new_position[1]] == "O":
            new_position = (position[0] + DIRECTIONS[instruction][0], position[1] + DIRECTIONS[instruction][1])

        if self.grid[new_position[0]][new_position[1]] in ["#", "."]:
            return True
        else:
            return new_position


    def draw(self, speed=0.1):
        aoc_common.draw_grid_to_console(self.grid, speed)


    def move(self, instruction):
        new_robot_position = self.move_target(instruction, self.robot_position)

        if self.grid[new_robot_position[0]][new_robot_position[1]] == "."
            



        if P1_DEBUG: print(f"Robot moving {instruction}")

        if self.grid[new_robot_position[0]][new_robot_position[1]] == "#":
            if P1_DEBUG: print(f"Robot at {self.robot_position} has hit a WALL at {new_robot_position} when moving {instruction}")

        elif self.grid[new_robot_position[0]][new_robot_position[1]] == "O":
            if P1_DEBUG: print(f"Robot at {self.robot_position} has hit a BOX at {new_robot_position} when moving {instruction}")
            self.box_move(instruction, new_robot_position)

        if self.grid[new_robot_position[0]][new_robot_position[1]] == ".":
            self.update_position(old_pos=self.robot_position, new_pos=new_robot_position)


def part1(grid, instructions):
    p1_warehouse = warehouse(grid)

    if P1_DEBUG: p1_warehouse.draw()
    for instruction in instructions:
        p1_warehouse.move(instruction)
        if P1_DEBUG: p1_warehouse.draw(1)
        print()


    if P1_DEBUG: p1_warehouse.draw(0.00001)
    return p1_warehouse.calculate_gps()


def part2(input):
    if P2_DEBUG: print(f"Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_grid = [list(x) for x in parsed_input[0].split("\n")]
    parsed_instructions = list("".join(parsed_input[1].split("\n")))

    start_time_part1 = time.time()
    part_1 = part1(parsed_grid, parsed_instructions)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
