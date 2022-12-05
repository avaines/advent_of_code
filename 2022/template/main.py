import os

INPUT_DEBUG = True
P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = False # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    if INPUT_DEBUG: print("Parsing the input")
    return input

def part1(input):
    if P1_DEBUG: print("Doing Part 1 things")
    return "part 1 answer"

def part2(input):
    if P2_DEBUG: print("Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    print()
    print("# # # SOLUTIONS # # #")

    part_1 = part1(parsed_input)
    print("Part1:", part_1 )
    print()
    
    part_2 = part2(parsed_input)
    print("Part2:", part_2 )
