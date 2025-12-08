# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms, aoc_grid_tools

P1_DEBUG = False
P1_ANIMATE=True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def fire_lazer(input):
    start_loc = (0, input[0].index('S'))

    current_beams = [0] * len(input[0])
    current_beams[start_loc[1]] = 1
    splits_encountered = 0

    for ri, r in enumerate(input):
        next_beams = [0] * len(input[0])

        for ci, _ in enumerate(r):
            if current_beams[ci] > 0:
                if input[ri][ci] == '^':
                    #  Split Beam
                    splits_encountered += 1
                    if P1_DEBUG: print(f"Beam at row {ri} col {ci} split by ^")

                    # Beam splits left and right
                    if ci - 1 >= 0:
                        next_beams[ci - 1] += current_beams[ci]
                        input[ri][ci - 1] = '|'

                    if ci + 1 < len(input[0]):
                        next_beams[ci + 1] += current_beams[ci]
                        input[ri][ci + 1] = '|'

                else:
                    # no split, beam goes down
                    next_beams[ci] += current_beams[ci]
                    input[ri][ci] = '|'

        if P1_ANIMATE: aoc_grid_tools.draw_grid_to_console(input, delay=0.12, headerText=f"Total beams {sum(current_beams)} at row {ri}")

        current_beams = next_beams

    return splits_encountered, sum(current_beams)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    FIRE = fire_lazer(parsed_input)

    start_time_part1 = time.time()
    part_1 = FIRE[0]
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = FIRE[1]
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
