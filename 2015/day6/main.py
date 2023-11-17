
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

p1_lighting_grid = aoc_algorithms.generate_grid(1000,1000, 0)
p2_lighting_grid = aoc_algorithms.generate_grid(1000,1000, 0)


def break_down_instruction(instruction):
    instruction = instruction.split(" ")
    if instruction[0] == "toggle":
        instruction.insert(0, "")
    return instruction


def operate_boolean_lights(action, start_light_grid_ref, end_light_grid_ref):
    start_light_grid_ref = start_light_grid_ref.split(",")
    end_light_grid_ref = end_light_grid_ref.split(",")

    for x in range(int(start_light_grid_ref[0]), int(end_light_grid_ref[0])+1):
        for y in range(int(start_light_grid_ref[1]), int(end_light_grid_ref[1])+1):
            # print(f"switch ({x},{y}): {p1_lighting_grid[x][y]} to {action}")

            if (action == "on" or action == "toggle") and p1_lighting_grid[x][y] == 0:
                p1_lighting_grid[x][y] = 1
            elif (action == "off" or action == "toggle") and p1_lighting_grid[x][y] == 1:
                p1_lighting_grid[x][y] = 0


def operate_variable_lights(action, start_light_grid_ref, end_light_grid_ref):
    start_light_grid_ref = start_light_grid_ref.split(",")
    end_light_grid_ref = end_light_grid_ref.split(",")

    for x in range(int(start_light_grid_ref[0]), int(end_light_grid_ref[0])+1):
        for y in range(int(start_light_grid_ref[1]), int(end_light_grid_ref[1])+1):
            # print(f"switch ({x},{y}): {p2_lighting_grid[x][y]} to {action}")

            if action == "on":
                p2_lighting_grid[x][y] += 1
            elif action == "off" and p2_lighting_grid[x][y] > 0:
                p2_lighting_grid[x][y] -= 1
            elif action == "toggle":
                p2_lighting_grid[x][y] += 2


def part1(input):
    for instruction in input:
        instruction = break_down_instruction(instruction)

        operate_boolean_lights(instruction[1], instruction[2], instruction[4])

    lights_on = 0
    for row in p1_lighting_grid:
        lights_on += sum(row)

    return lights_on


def part2(input):
    for instruction in input:
        instruction = break_down_instruction(instruction)

        operate_variable_lights(instruction[1], instruction[2], instruction[4])

    lights_on = 0
    for row in p2_lighting_grid:
        lights_on += sum(row)

    return lights_on


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
