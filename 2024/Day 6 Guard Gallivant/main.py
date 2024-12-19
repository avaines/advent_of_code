# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import copy
import collections


P1_DEBUG = False
P1_DRAW = False
P2_DEBUG = True
P2_DRAW = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


class puzzle:
    guard_directions = { "^":[-1, 0], "v":[1, 0], ">":[0,1], "<":[0, -1] }

    def __init__(self, map, draw_path=False):
        self.map = map
        self.guard_direction = "^"
        self.guard_position = self.findGuard()
        self.guard_path_taken = [self.guard_position]
        self.wall_from_orientation = {"^":[self.guard_position], ">":[], "v":[], "<":[]} # part 2
        self.draw_path = draw_path
        self.guard_on_map = True


    def findGuard(self):
        for ri, r in enumerate(self.map):
            for ci, c in enumerate(r):
                if self.map[ri][ci] == self.guard_direction:
                    if P1_DEBUG: print(f"Guard {self.map[ri][ci]}, found at map ref {ri},{ci}")
                    self.guard_on_map = True
                    return (ri,ci)

    def rotate(self):
        match self.guard_direction:
            case "^":
                self.guard_direction = ">"
                wall_offset = self.guard_directions["^"]
                wall_position = (self.guard_position[0] + wall_offset[0], self.guard_position[1] + wall_offset[1])
                self.wall_from_orientation["^"].append(wall_position)

            case ">":
                self.guard_direction = "v"
                wall_offset = self.guard_directions[">"]
                wall_position = (self.guard_position[0] + wall_offset[0], self.guard_position[1] + wall_offset[1])
                self.wall_from_orientation[">"].append(wall_position)

            case "v":
                self.guard_direction = "<"
                wall_offset = self.guard_directions["v"]
                wall_position = (self.guard_position[0] + wall_offset[0], self.guard_position[1] + wall_offset[1])
                self.wall_from_orientation["v"].append(wall_position)

            case "<":
                self.guard_direction = "^"
                wall_offset = self.guard_directions["<"]
                wall_position = (self.guard_position[0] + wall_offset[0], self.guard_position[1] + wall_offset[1])
                self.wall_from_orientation["<"].append(wall_position)


    def is_in_bounds(self, coords:tuple[int,int]):
        if 0 <= coords[0] < len(self.map):
           if 0 <= coords[1] < len(self.map[0]):
               return True
        return False


    def move(self, next_block):
        next_block = self.guard_directions[self.guard_direction]

        self.guard_path_taken.append(self.guard_position)
        self.map[self.guard_position[0]][self.guard_position[1]] = "X"

        self.guard_position = (self.guard_position[0] + next_block[0], self.guard_position[1] + next_block[1])
        self.map[self.guard_position[0]][self.guard_position[1]] = self.guard_direction


    def move_guard(self):
        offset = self.guard_directions[self.guard_direction]
        next_block = (self.guard_position[0] + offset[0], self.guard_position[1] + offset[1])

        if not self.is_in_bounds(next_block):
            self.guard_on_map = False
            if P1_DEBUG: print(f"Next block at {self.guard_position}, traveling {self.guard_direction} is out of bounds")
            self.guard_path_taken.append(next_block)
        elif self.map[next_block[0]][next_block[1]] in ["#", "O"]:
            self.rotate()
        else:
            self.move(next_block)

        if self.draw_path: aoc_common.draw_grid_to_console(self.map)


def part1(input):
    area_map = copy.deepcopy(input)
    patrol_p1 = puzzle(area_map, P1_DRAW)

    while patrol_p1.guard_on_map:
        patrol_p1.move_guard()

    return len(set(patrol_p1.guard_path_taken))


def part2(input):
    max_num_positions = len(input) * len(input[0])
    positions_checked = 0
    p2_walls = []

    for ci, col in enumerate(input):
        for ri, r in enumerate(col):
            positions_checked+=1

            if input[ci][ri] == ".":
                potential_map = copy.deepcopy(input)
                potential_map[ci][ri] = "O"

                patrol_p2 = puzzle(potential_map, P2_DRAW)
                # patrol.drawPathToConsole()

                while patrol_p2.guard_on_map:
                    if 5 in collections.Counter(patrol_p2.guard_path_taken).values():
                        if P2_DEBUG: print(f"Progress {(positions_checked/max_num_positions)*100}%")
                        p2_walls.append(([ci],[ri]))
                        break
                    patrol_p2.move_guard()

    return len(p2_walls)




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

