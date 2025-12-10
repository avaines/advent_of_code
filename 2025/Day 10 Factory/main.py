# pylint: disable-all
# Import AOC Common
from ast import comprehension
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools
from itertools import combinations
from scipy.optimize import linprog


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def draw_state(state):
    lights = []
    for i in state:
        lights.append("." if i == 0 else "#")
    return("".join(lights))


def part1(input):
    shortest_combos = []
    for lights, buttons,_ in input:
        valid_combos = []

        for n in range(len(buttons)):
            for button_combo in combinations(buttons, n):
                state = [sum(i in x for x in button_combo) % 2
                            for i in range(len(lights))]

                if state == lights:
                    valid_combos.append(button_combo)
                    if P1_DEBUG: print(f"State: {draw_state(state)} (expecting {draw_state(lights)}), Buttons: {button_combo}")

        shortest_combos.append(len(min(valid_combos, key=len)))

    return sum(shortest_combos)


def part2(input):
    shortest_combos = []

    for _, buttons, joltages in input:
        # 'The coefficients of the linear objective function to be minimized' for SciPy - all buttons cost 1
        coefficient = [1 for _ in buttons]

        # Build 'equality constraint matrix' for SciPy - basically each row represents which buttons affect each light
        ecm = []
        for i in range(len(joltages)):
            ecm.append([1 if i in b else 0 for b in buttons])

        # Do the thing, minimize the number of buttons pressed while achieving the target joltages
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
        shortest_combos.append(int(linprog(coefficient, A_eq=ecm, b_eq=joltages, integrality=1).fun))

    return sum(shortest_combos)


def unpack_input(input):
    parsed_input = []
    for line in input:
        lights, *buttons, joltage = line.split()
        # lights = list(lights.strip('[]'))
        lights = [0 if c == '.' else 1 for c in lights.strip('[]')] # make it a boolean its easier to check later
        buttons = [tuple(int(x) for x in button[1:-1].split(',')) for button in buttons]
        joltage = tuple(int(c) for c in joltage[1:-1].split(','))
        parsed_input.append((lights, buttons, joltage))

    return parsed_input

if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = unpack_input(parsed_input)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
