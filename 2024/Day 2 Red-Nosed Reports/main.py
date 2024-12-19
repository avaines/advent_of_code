# pylint: disable-all
# Import AOC Common
import os
import sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def is_sorted(lst:list):
    if all(lst[i] <= lst[i+1] and 1 <= abs(lst[i] - lst[i+1]) <=3 for i in range(len(lst) -1)):
        # if P1_DEBUG: print(f"{lst} is sorted in Ascending order")
        return "ASC"
    elif all(lst[i] >= lst[i+1] and 1 <= abs(lst[i] - lst[i+1]) <=3 for i in range(len(lst) -1)):
        # if P1_DEBUG: print(f"{lst} is sorted in Descending order")
        return "DESC"
    else:
        return False


def part1(input):
    num_safe_reports=0

    for report in input:
        split_report = [int(i) for i in report.split()]

        if not is_sorted(split_report):
            if P1_DEBUG: print(f"{split_report} is Unsafe")
        else:
            if P1_DEBUG: print(f"{split_report} is Safe")
            num_safe_reports+=1

    return num_safe_reports


def part2(input):
    num_safe_reports=0

    for report in input:
        split_report = [int(i) for i in report.split()]

        if not is_sorted(split_report):
            # if P2_DEBUG: print(f"{split_report} is Unsafe")
            for i in range(len(split_report)):
                if is_sorted([x for l,x in enumerate(split_report) if l!=i]):
                    if P2_DEBUG: print(f"{split_report} is Safe when {i}({split_report[i]}) is dropped")
                    num_safe_reports+=1
                    break
        else:
            num_safe_reports+=1

    return num_safe_reports


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part 1:", part_1 )
    print("Part 2:", part_2 )
