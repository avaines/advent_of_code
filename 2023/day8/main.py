# pylint: disable-all
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import itertools as it
from math import lcm


P1_DEBUG = False
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False
if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(directions, node_map):
    current_location = "AAA"
    number_of_steps = 0

    for direction in it.cycle(directions):
        number_of_steps += 1

        if direction == "L":
            current_location = node_map[current_location][0]
            if P1_DEBUG: print(f"From {current_location}, taking the LEFT instruction to {node_map[current_location][0]}")
        else:
            current_location = node_map[current_location][1]
            if P1_DEBUG: print(f"From {current_location}, taking the RIGHT instruction to {node_map[current_location][1]}")

        if current_location == "ZZZ":
            break

    return number_of_steps


def part2(directions, node_map):
    def part2_sub(node):
        number_of_steps = 0

        for direction in it.cycle(directions):
            number_of_steps += 1

            if direction == 'L':
                next_node = node_map[node][0]
                if P2_DEBUG: print(f"From {node}, taking the LEFT instruction to {next_node}")
            else:
                next_node = node_map[node][1]
                if P2_DEBUG: print(f"From {node}, taking the RIGHT instruction to {next_node}")

            node = next_node
            if node.endswith('Z'):
                return number_of_steps

    path_tracker = [node for node in node_map if node.endswith("A")]
    lcms = [part2_sub(node) for node in path_tracker]

    return lcm(*lcms)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    node_map = {}
    for instruction in parsed_input[1].splitlines():
        key, nodes = instruction.split(" = ")
        nodes = nodes[1:-1].split(", ")
        node_map[key] = nodes

    part_1 = part1(parsed_input[0], node_map)
    part_2 = part2(parsed_input[0], node_map)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
