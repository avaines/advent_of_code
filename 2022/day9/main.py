import os
import math

INPUT_DEBUG = True
P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    instructions = list(map(str.split, input))
    return instructions

def part1(input):
    directions = { "U":[0, 1], "D":[0, -1], "L":[-1, 0], "R":[1, 0] }
    tail_steps_taken = set()
    head_coords = [0, 0]
    tail_coords = [0, 0]

    for instruction in input:
        for step in range(int(instruction[1])):
            if P1_DEBUG: print("Moving", step, "of", instruction[1], "steps to the", instruction[0], "direction")
            # move head to new coords
            head_coords_before_move = head_coords
            head_coords = [x + y for x, y in zip(head_coords, directions[instruction[0]])]

            distance = math.dist(head_coords, tail_coords)
            if distance >= 2:
                tail_coords = head_coords_before_move

            tail_steps_taken.add(tuple(tail_coords))

        previous_move = directions[instruction[0]]
    return len(tail_steps_taken)

def part2(input):
    directions = { "U":[0, 1], "D":[0, -1], "L":[-1, 0], "R":[1, 0] }
    tail_steps_taken = set()
    knots=[[0,0]]*10

    for instruction in input:
        for step in range(int(instruction[1])):
            knots[0] = [x + y for x, y in zip(knots[0], directions[instruction[0]])]

            for i in range(1, len(knots)):
                x_dist = knots[i-1][0] - knots[i][0]
                y_dist = knots[i-1][1] - knots[i][1]
                if abs(x_dist) >= 2 or abs(y_dist) >= 2:
                    # build the new coordinate for the specific knot
                    knots[i] = [knots[i][0] + min(max(x_dist, -1), 1), knots[i][1] + min(max(y_dist, -1), 1)]

            tail_steps_taken.add(tuple(knots[-1]))

    return len(tail_steps_taken)


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )