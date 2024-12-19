import os
import operator

INPUT_DEBUG = True
P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    if INPUT_DEBUG: print("Parsing the input")
    elf_id = 1
    calories_carried = 0
    elf_to_calories_dict = dict()

    for calories in input:
        if calories != '':
            calories_carried += int(calories)
        else:
            # Null line is end of an elf's calorie supply.
            elf_to_calories_dict[elf_id] = calories_carried
            # Reset/adjust counters
            elf_id += 1
            calories_carried = 0

    return elf_to_calories_dict

def part1(input):
    # if P1_DEBUG: print("Doing Part 1 things")
    most_calories = max(input, key=input.get)

    if P1_DEBUG: print("Elf number %s is carrying the most calories (%s)" % (most_calories, input[most_calories]) )
    return most_calories, input[most_calories]

def part2(input):
    # if P2_DEBUG: print("Doing Part 2 things")
    top_3_elves_calories = 0

    # Top most calories
    most_calories = max(input, key=input.get)
    top_3_elves_calories += input[most_calories]
    input.pop(most_calories)

    # second top most calories
    most_calories = max(input, key=input.get)
    top_3_elves_calories += input[most_calories]
    input.pop(most_calories)

    # third top most calories
    most_calories = max(input, key=input.get)
    top_3_elves_calories += input[most_calories]
    input.pop(most_calories)

    return top_3_elves_calories

    return "part 2 answer"


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)

    part_2 = part2(parsed_input)

    print()
    print("# # # SOLUTIONS # # #")
    print("Part1: How many total Calories is that Elf carrying?")
    print("Elf %s is carrying the most calories (%s)" % (part_1[0], part_1[1]) )
    print()
    print("Part2: How many Calories are those Elves carrying in total?")
    print(part_2 )
