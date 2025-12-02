# pylint: disable-all
# Import AOC Common
import os
import string
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


def part1(input):
    invalidIds = []
    for check in input.split(","):
        a,b=check.split("-")
        valsToCheck = set(range(int(a),int(b)+1))
        for valToCheck in valsToCheck:
            x = str(valToCheck)
            firstHalf, seconfHalf = x[:len(x)//2], x[len(x)//2:]
            if firstHalf == seconfHalf:
                if P1_DEBUG: print(f"Found an invalid ID!: {valToCheck}")
                invalidIds.append(valToCheck)

    return sum(invalidIds)


def part2(input):
    invalidIds = []
    for check in input.split(","):
        a,b=check.split("-")
        valsToCheck = set(range(int(a),int(b)+1))
        for valToCheck in valsToCheck:

            # split in to blocks of 1, through up to half the length of the value
            for blockSize in range(1, (len(str(valToCheck))//2)+1):
                # get the block size chunk from the start
                x = str(valToCheck)
                firstBlock = x[:blockSize]

                # the rest of the block should be made up of this block repeated
                restOfValue = x[blockSize:]

                # check the restOfValue is devisible by the blockSize
                if len(restOfValue) % blockSize != 0:
                    continue

                repeatsNeeded = len(restOfValue) // blockSize
                if firstBlock * repeatsNeeded == restOfValue:
                    if P2_DEBUG: print(f"Found an invalid ID!: {valToCheck} with block size {blockSize}")
                    invalidIds.append(valToCheck)
                    # break


    return sum(list(set(invalidIds))) # lazy dedupe


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input[0])
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input[0])
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
