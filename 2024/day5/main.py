# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def is_valid_order(rules, pages):
    for i, page in enumerate(pages):
        for page_rule in rules.get(page,[]): #For each of the rules for this page number
            if page_rule in pages[:i]: # if the current rule for this page is in the look ahead page updates list
                if P1_DEBUG: print(f"Page {page} looks wrong because there is a rule that says it needs to be in front of page {page_rule}...")
                return False
    return True


def part1(rules, page_updates):
    rule_map = {}
    for rule in rules:
        if rule[0] in rule_map:
            rule_map[rule[0]].append(rule[1])
        else:
            rule_map[rule[0]] = [rule[1]]

    invalid_updates = [pages for pages in page_updates if is_valid_order(rule_map, pages)]

    total = 0
    for invalid_updates in invalid_updates:
        total+=invalid_updates[len(invalid_updates)//2]

    return total


def part2(rules, page_updates):
    rule_map = {}
    for rule in rules:
        if rule[0] in rule_map:
            rule_map[rule[0]].append(rule[1])
        else:
            rule_map[rule[0]] = [rule[1]]

    valid_updates = []
    for pages in page_updates:
        if not is_valid_order(rule_map, pages):
            # Turns out this is a perfect case for Kaaaaaaahn's Topological Sort algorythm
            # "The canonical application of topological sorting is in scheduling a sequence of jobs or tasks based on their dependencies."
            # (thanks Reddit)

            valid_updates.append(aoc_algorithms.topological_sort_khans(set(pages),rule_map))

    total = 0
    for valid_update in valid_updates:
        total+=valid_update[len(valid_update)//2]

    return total


if __name__ == '__main__':
    page_ordering_rules, page_updates = aoc_common.import_two_part_input(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, "|", ",")
    page_ordering_rules = aoc_common.convert_list_of_lists_to_ints(page_ordering_rules)
    page_updates = aoc_common.convert_list_of_lists_to_ints(page_updates)

    start_time_part1 = time.time()
    part_1 = part1(page_ordering_rules, page_updates)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(page_ordering_rules, page_updates)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
