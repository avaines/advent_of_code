# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG = True
P2_DEBUG = False

USE_REAL_DATA = False # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


class puzzle:
    guard_directions = { "^":[-1, 0], "v":[1, 0], ">":[0,1], "<":[0, -1] }

    def __init__(self, map, draw_path=False):
        self.map = map
        self.guard_direction = "^"
        self.guard_on_map = False
        self.guard_position = self.findGuard()
        self.guard_path_taken = []
        self.draw_path = draw_path
        self.p2_walls = []

    def findGuard(self):
        for ri, r in enumerate(self.map):
            for ci, c in enumerate(r):
                if self.map[ri][ci] == self.guard_direction:
                    if P1_DEBUG: print(f"Guard {self.map[ri][ci]}, found at map ref {ri},{ci}")
                    self.guard_on_map = True
                    return (ri,ci)


    def drawPathToConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.map:
            print(''.join(row))
        time.sleep(0.1)

    def moveGuard(self):
        if self.guard_on_map:
            if self.draw_path: self.drawPathToConsole()
            offset = self.guard_directions[self.guard_direction]
            new_guard_location = (self.guard_position[0] + offset[0], self.guard_position[1] + offset[1])

            if 0 < new_guard_location[0] >= len(self.map) or 0 < new_guard_location[1] > len(self.map[0]):
               if P1_DEBUG: print(f"Guard has exited the map at found at map ref {new_guard_location}, traveling {self.guard_direction}")
               self.guard_path_taken.append(self.guard_position)
               self.guard_on_map = False

            else:
                if self.map[new_guard_location[0]][new_guard_location[1]] == "#":
                    match self.guard_direction: # Rotate 'right'
                        case "^": self.guard_direction = ">"
                        case ">": self.guard_direction = "v"
                        case "v": self.guard_direction = "<"
                        case "<": self.guard_direction = "^"

                    self.map[self.guard_position[0]][self.guard_position[1]] = self.guard_direction
                    if self.draw_path: self.drawPathToConsole()
                    if P1_DEBUG: print(f"Guard has hit a wall at ({new_guard_location[0]},{new_guard_location[1]}); turning around instead, now facing {self.guard_direction}")

                else:
                    # Part 2
                    # Would turning here result in the next move being one we've seen before?
                    match self.guard_direction: # Rotate 'right'
                        case "^":
                            ghost_guard_direction = ">"
                            ghost_guard_next_position = (self.guard_position[0],self.guard_position[1]+1)
                            ghost_projected_path=self.map[ghost_guard_next_position[0]][ghost_guard_next_position[1]:]

                        case ">":
                            ghost_guard_direction = "v"
                            ghost_guard_next_position = (self.guard_position[0]+1,self.guard_position[1])
                            ghost_projected_path = [self.map[i][ghost_guard_next_position[1]] for i in range(ghost_guard_next_position[0], len(self.map))]

                        case "v":
                            ghost_guard_direction = "<"
                            ghost_guard_next_position = (self.guard_position[0],self.guard_position[1]-1)
                            ghost_projected_path=list(reversed(self.map[ghost_guard_next_position[0]][:ghost_guard_next_position[1]+1]))

                        case "<":
                            ghost_guard_direction = "^"
                            ghost_guard_next_position = (self.guard_position[0]-1,self.guard_position[1])
                            ghost_projected_path = list(reversed([self.map[i][ghost_guard_next_position[1]] for i in range(0, ghost_guard_next_position[0])]))

                    # if we followed the ghosts projected path, there should be an X touching an # somewhere to identify a loop
                    if any(ghost_projected_path[i] == 'X' and ghost_projected_path[i + 1] == '#' for i in range(len(ghost_projected_path) - 1)):
                        # self.map[self.guard_position[0] + offset[0]][self.guard_position[1] + offset[1]] = "O"
                        self.p2_walls.append((self.guard_position[0] + offset[0], self.guard_position[1] + offset[1]))
                        if self.draw_path: self.drawPathToConsole()
                        if P2_DEBUG: print(f"Ghost Guard would be back on a previously visited track if they turned at ({new_guard_location[0]},{new_guard_location[1]})")

                    self.guard_path_taken.append(self.guard_position)
                    self.map[self.guard_position[0]][self.guard_position[1]] = "X"

                    self.guard_position = new_guard_location
                    self.map[self.guard_position[0]][self.guard_position[1]] = self.guard_direction

                    if self.draw_path: self.drawPathToConsole()
                    if P1_DEBUG: print(f"Guard has moved to ({new_guard_location[0]},{new_guard_location[1]}), {len(self.guard_path_taken)} steps taken")

if __name__ == '__main__':
    DRAW_IT=False
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    p1_puzzle = puzzle(parsed_input, DRAW_IT)

    while p1_puzzle.guard_on_map:
        p1_puzzle.moveGuard()

    end_time_part1 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"⏱️  in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 1: {len(set(p1_puzzle.guard_path_taken))}")
    print(f"Part 2: {len(p1_puzzle.p2_walls)}")