# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG = False
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

class dial():
    _positions = list(range(0,100))

    def __init__(self, initialPosition=50):
        self.current_position = initialPosition

    def turn(self, direction, steps):
        length = len(self._positions)
        rollovers = 0

        match direction:
            case "R":
                # P2 swapout
                # self.current_position = (self.current_position + steps) % len(self._positions)

                # P2 swapin
                # Count every position from current to current+steps, how many times do we hit 0?
                for i in range(1, steps + 1):
                    if (self.current_position + i) % length == 0:
                        rollovers += 1

                self.current_position = (self.current_position + steps) % length

            case "L":
                # P2 swapout
                # self.current_position = (self.current_position - steps) % len(self._positions)

                # P2 swapin
                for i in range(1, steps + 1):
                    if (self.current_position - i) % length == 0:
                        rollovers += 1

                self.current_position = (self.current_position - steps) % length

        return self.current_position, rollovers


def part1(input):
    p1_dial = dial()
    counter = 0

    for instruction in input:
        direction = instruction[0]
        steps = int(instruction[1:])
        p1_dial.turn(direction, steps)

        if P1_DEBUG: print(f"The dial is rotated {instruction} to point at {p1_dial.current_position}.")

        if p1_dial.current_position == 0:
            counter += 1
    return counter


def part2(input):
    p2_dial = dial()
    counter = 0
    total_rollovers = 0

    for instruction in input:
        direction = instruction[0]
        steps = int(instruction[1:])
        current_position, rollovers = p2_dial.turn(direction, steps)

        if rollovers > 0:
            if P2_DEBUG: print(f"The dial is rotated {instruction} to point at {current_position}. During this rotation it points at 0 {rollovers} times.")
            total_rollovers += rollovers
        else:
            if P2_DEBUG: print(f"The dial is rotated {instruction} to point at {current_position}.")

        if current_position == 0:
            counter += 1

    return total_rollovers

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
