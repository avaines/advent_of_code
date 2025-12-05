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


def part1(input):
    ingredientRanges = input[0]
    ingredientIds = input[1]
    freshIngredients = set()

    for ingredientId in [int(x) for x in ingredientIds]:
        for ingredientRange in ingredientRanges:
            lower,upper = [int(x) for x in ingredientRange.split("-")]

            if ingredientId >= lower and ingredientId <= upper:
                if P1_DEBUG: print(f"Ingredient ID {ingredientId} is fresh because it falls into range {ingredientRange}")
                freshIngredients.add(ingredientId)
                continue

    return len(freshIngredients)


def part2(input):
    ingredientRanges = [tuple(map(int,x.split("-"))) for x in input[0]]
    freshIngredientCount = 0
    lowestIngredientId = 0

    # loop through sorted Ing.Id ranges, skip double-counting overlapping regions
    for lower, upper in sorted(ingredientRanges):
        freshIngredientCount += len(range(max(lower, lowestIngredientId), upper + 1))
        lowestIngredientId = max(upper + 1, lowestIngredientId)

    return freshIngredientCount


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_two_sections_double_new_line_separator(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
