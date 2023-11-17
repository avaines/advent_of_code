
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import re

P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def is_nice(string):
    if len(re.findall(r'[aeiou]', string)) < 3: return False
    if not bool(re.search(r'(\w)\1', string)): return False
    if bool(re.search(r'(ab|cd|pq|xy)', string)): return False
    return True

def is_nice_v2(string):
    if not bool(re.search(r'(\w\w).*\1', string)): return False
    if not bool(re.search(r'(\w)\w\1', string)): return False
    return True

def part1(input):
    nice_strings = []
    for string in input:
        if is_nice(string):
            if P1_DEBUG: print(f"{string}, is nice")
            nice_strings.append(string)
        else:
            if P1_DEBUG: print(f"{string}, is naughty")

    return len(nice_strings)

def part2(input):
    nice_strings = []
    for string in input:
        if is_nice_v2(string):
            if P2_DEBUG: print(f"{string}, is nice")
            nice_strings.append(string)
        else:
            if P2_DEBUG: print(f"{string}, is naughty")

    return len(nice_strings)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
