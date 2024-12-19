import os

INPUT_DEBUG = False
P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    parsed_input = []

    for row in input:

        elf_group_assignments = []
        for elf_group in row.split(","):
            this_elf_assignment_range = []
            start_num,end_num = map(int, elf_group.split('-'))
            this_elf_assignment_range += range(start_num, end_num+1)
            if INPUT_DEBUG: print("This elf group of:", elf_group, "starts at ", start_num, "ends at", end_num, " for a range of", this_elf_assignment_range)
            elf_group_assignments.append(this_elf_assignment_range)

        parsed_input.append(elf_group_assignments)
        # parsed_input is now a list of lists, each containing multiple lists (one for each elf)
    return parsed_input

def part1(input):
    subsets = 0
    for elf_pair in input:
        if set(elf_pair[0]).issubset(elf_pair[1]) or set(elf_pair[1]).issubset(elf_pair[0]):
            if P1_DEBUG: print("Found a subset", elf_pair)
            subsets += 1
    return subsets


def part2(input):
    subsets = 0
    for elf_pair in input:
        if set(elf_pair[0]).intersection(elf_pair[1]) or set(elf_pair[1]).intersection(elf_pair[0]):
            if P2_DEBUG: print("Found an intersection in", elf_pair, )
            subsets += 1
    return subsets


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)

    part_2 = part2(parsed_input)

    print()
    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
