# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from collections import defaultdict


P1_DEBUG = False
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample1.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input, iterations):
    last_ten_secrets = defaultdict(lambda: {i: None for i in range(1, 11)})

    for initial_secret_number in input:
        current_secret_value = initial_secret_number

        for i in range(iterations):
            # Calculate the result of multiplying the secret number by 64.
            #   Then, mix this result into the secret number.
            #   Finally, prune the secret number.
            current_secret_value ^= (current_secret_value*64)
            current_secret_value %= 16777216

            # Calculate the result of dividing the secret number by 32.
            #   Round the result down to the nearest integer.
            #   Then, mix this result into the secret number.
            #   Finally, prune the secret number.
            current_secret_value ^= (current_secret_value//32)
            current_secret_value %= 16777216

            # Calculate the result of multiplying the secret number by 2048.
            #   Then, mix this result into the secret number.
            #   Finally, prune the secret number.
            current_secret_value ^= (current_secret_value*2048)
            current_secret_value %= 16777216

            last_ten_secrets[initial_secret_number][i%10+1] = current_secret_value

    if P1_DEBUG:
        for s in last_ten_secrets:
            print(f"Secret {s}: {last_ten_secrets[s][10]}")
            # S:123
            #   15887950
            #   16495136
            #   527345
            #   704524
            #   1553684
            #   12683156
            #   11100544
            #   12249484
            #   7753432
            #   5908254

            # 1: 8685429
            # 10: 4700978
            # 100: 15273692
            # 2024: 8667524

    total = sum([last_ten_secrets[secret][10] for secret in last_ten_secrets])
    return total


def part2(input):
    if P2_DEBUG: print(f"Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    parsed_input = [int(x) for x in parsed_input]

    start_time_part1 = time.time()
    part_1 = part1(parsed_input, iterations=2000)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
