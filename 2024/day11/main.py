# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import copy
from functools import cache

P1_DEBUG = False
P2_DEBUG = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

@cache
def parts(stone, blink):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    if blink == BLINKS:
        return 1

    if stone == 0:
        if P1_DEBUG: print(f"\tStone {stone} replacing with a '1'")
        return parts(1, blink+1)

    elif len(str(stone))%2 == 0:
        first_stone, second_stone = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
        if P1_DEBUG: print(f"\tStone {stone} splitting in to two stones, {first_stone} and {second_stone}")
        return parts(int(first_stone), blink+1) + parts(int(second_stone), blink+1)

    else:
        if P1_DEBUG: print(f"\tStone {stone} doesn't fit any rule, multiplying by 2024, {stone*2024}")
        return parts(stone * 2024, blink +1)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    line_of_stones = list(map(int,parsed_input[0].split()))

    start_time_part1 = time.time()
    BLINKS = 25 if USE_REAL_DATA else 6
    part_1 = sum(parts(stone, 0) for stone in line_of_stones)
    end_time_part1 = time.time()

    parts.cache_clear()
    start_time_part2 = time.time()
    BLINKS = 75 if USE_REAL_DATA else 6
    part_2 = sum(parts(stone, 0) for stone in line_of_stones)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
