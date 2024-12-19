from multiprocessing.dummy import current_process
import os

# Import the elfcomm3000 class
import sys
sys.path.append("../")
from shared.device import ElfComm3000


INPUT_DEBUG = True
P1_DEBUG    = False
P2_DEBUG    = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    if INPUT_DEBUG: print("Parsing the input")
    return input

def part1(input):
    elfcom3000 = ElfComm3000(
        debug = P1_DEBUG,
        inspection_cycles = [20, 60, 100, 140, 180, 220],
    )

    for instruction in input:
        elfcom3000.execute_instruction(instruction)

        if P1_DEBUG: print("ElfCom3000 has run", elfcom3000.cycle, "cycles; the current value of register_x is:", elfcom3000.register_x)

    return sum(elfcom3000.signal_strength_at_inspection)

def part2(input):
    elfcom3000 = ElfComm3000(
        debug = P2_DEBUG
    )

    for instruction in input:
        elfcom3000.execute_instruction(instruction)

    print(elfcom3000.crt_render())
    print()


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    part_2 = part2(parsed_input)