import os
import string

INPUT_DEBUG = True
P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    if INPUT_DEBUG: print("Parsing the input")
    return input

def part1(input):
    total_priority = 0

    for rucksack in input:
        compartment_1, compartment_2 = list(rucksack[:len(rucksack)//2]), list(rucksack[len(rucksack)//2:])
        duplicate_items = set(compartment_1) & set(compartment_2)

        for duplicate_item in duplicate_items:
            if duplicate_item.islower():
                total_priority += string.ascii_lowercase.index(duplicate_item) +1
            else:
                total_priority += string.ascii_uppercase.index(duplicate_item) +27

    return total_priority

def part2(input):
    total_priority_of_badge_items = 0
    current_group_of_3_start_index = 0

    while current_group_of_3_start_index <= len(input) -3:
        badge_items = set(input[current_group_of_3_start_index]) & set(input[current_group_of_3_start_index+1]) & set(input[current_group_of_3_start_index+2])
        if P2_DEBUG: print("The matching badge is", badge_items)

        for badge_item in badge_items:
            if badge_item.islower():
                total_priority_of_badge_items += string.ascii_lowercase.index(badge_item) +1
            else:
                total_priority_of_badge_items += string.ascii_uppercase.index(badge_item) +27
        current_group_of_3_start_index += 3

    return total_priority_of_badge_items


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)

    part_2 = part2(parsed_input)

    print()
    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
