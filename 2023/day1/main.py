
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import regex

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False
if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data(2023, 1)

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def part1(input):
    raw_instructions = []
    for line in input:
        digits = [int(s) for s in [*line] if s.isdigit()]
        raw_instructions.append( f"{digits[0]}{digits[-1]}")

    return sum(list(map(int, raw_instructions)))


def part2(input):
    raw_instructions = []
    for line in input:
        line_words = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        for i, entry in enumerate(line_words):
            match entry:
                case "one":
                    line_words[i] = "1"
                case "two":
                    line_words[i] = "2"
                case "three":
                    line_words[i] = "3"
                case "four":
                    line_words[i] = "4"
                case "five":
                    line_words[i] = "5"
                case "six":
                    line_words[i] = "6"
                case "seven":
                    line_words[i] = "7"
                case "eight":
                    line_words[i] = "8"
                case "nine":
                    line_words[i] = "9"

        digits = [int(s) for s in [*line_words] if s.isdigit()]
        raw_instructions.append( f"{digits[0]}{digits[-1]}")

    return sum(list(map(int, raw_instructions)))


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )