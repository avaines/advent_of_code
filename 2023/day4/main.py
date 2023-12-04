
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    total = 0

    for card in input:
        winning_numbers = [i for i in input[card][0] if i in input[card][1]]
        total += int(2** (len(winning_numbers) -1))

    return total


def part2(input):
    # Keep track of the number of cards with a list and add new instances of each card spawned as a win, sum that to give number of winning cards
    num_of_ties = [1] * len(input)

    for i, card in enumerate(input):
        winning_numbers = [n for n in input[card][0] if n in input[card][1]]

        for j in range(i + 1, i + len(winning_numbers) + 1):
            num_of_ties[j] += num_of_ties[i]

    return sum(num_of_ties)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input_dict = aoc_common.three_part_parse_dict(parsed_input,": ", " | ")

    part_1 = part1(parsed_input_dict)
    part_2 = part2(parsed_input_dict)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
