# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from itertools import product


P1_DEBUG = False
P2_DEBUG = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample2.txt" % os.path.dirname(os.path.realpath(__file__))


def evaluate(numbers:list[int], operators:list, solution:int):
    result = numbers[0]

    for i, operator in enumerate(operators):
        match operator:
            case "+":
                result += numbers[i + 1]
            case "*":
                result *= numbers[i + 1]
            case "||":
                # Thanks StackOverflow...
                digits = 0
                tmp = numbers[i + 1]
                while tmp > 0:
                    tmp //= 10
                    digits += 1

                result = result * (10**digits) + numbers[i + 1]

        if result > solution:
            return -1

    return result


def part1(equations):
    total = 0

    for result, numbers in equations:
        for operators in product(["+", "*"], repeat=len(numbers) - 1): # product('ABCD', 'xy') -> Ax Ay Bx By Cx Cy Dx Dy
            if P1_DEBUG: print(f"Doing {numbers}, {operators} to equal {result}")
            if evaluate(numbers, operators, result) == result:
                if P1_DEBUG: print(f"\t{result} achieved with {numbers}, {operators}\n")
                total+=result
                break

    return total


def part2(equations):
    total = 0

    for result,numbers in equations:
        for operators in product(["+", "*", "||"], repeat=len(numbers) - 1):
            if P2_DEBUG: print(f"Doing {numbers}, {operators} to equal {result}")
            if evaluate(numbers, operators, result) == result:
                if P2_DEBUG: print(f"\t{result} achieved with {numbers}, {operators}\n")
                total+=result
                break

    return total


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    parsed_inputs = []

    for i in parsed_input:
        tmp=i.split(": ")
        parsed_inputs.append([int(tmp[0]),list(map(int, tmp[1].split(" ")))])

    start_time_part1 = time.time()
    part_1 = part1(parsed_inputs)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_inputs)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
