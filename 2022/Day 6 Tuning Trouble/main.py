import os

# Import the communications_system class
import sys
sys.path.append("../")
from shared.device import Communications_System

INPUT_DEBUG = True
P1_DEBUG    = True
P2_DEBUG    = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    return input

def part1(input):
    device = Communications_System(input, P1_DEBUG)
    return device.start_of_packet_marker

def part2(input):
    device = Communications_System(input, P2_DEBUG)
    return device.start_of_message_marker


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read())

    print()
    print("# # # SOLUTIONS # # #")

    part_1 = part1(parsed_input)
    print("Part1:", part_1 )
    print()

    part_2 = part2(parsed_input)
    print("Part2:", part_2 )
