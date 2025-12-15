# pylint: disable-all
'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_common
'''
import os
import requests
import re
import time

COOKIE_CACHE = "../../COOKIE"


def get_aoc_puzzle_data():
    ''' Get the puzzle data for a given puzzle using the cookie
       either enter it on each run or set the ENV VAR AOC_COOKIE '''
    path_extract = re.search(r'/(\d{4})/Day (\d+).*', os.path.dirname(__file__))

    if not os.path.exists('input.txt'):
        year = path_extract.group(1)
        day = path_extract.group(2)

        print(f"Downloading input for AOC {year}, day {day}")

        if os.path.exists(COOKIE_CACHE):
            with open(COOKIE_CACHE, "r") as cache_file:
                session_cookie = cache_file.read().strip()
                print("Using cached session cookie.")
        else:
            session_cookie = input("Enter your Advent of Code session cookie: ")
            with open(COOKIE_CACHE, "w") as cache_file:
                cache_file.write(session_cookie)
                print("Session cookie cached.")

        # Connect to the Advent of Code API to get puzzle details
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        headers = {"Cookie": f"session={session_cookie}"}

        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the data to input.txt
            with open('input.txt', 'w') as file:
                file.write(response.text.rstrip('\n'))

            print("Puzzle input saved to 'input.txt'")
        else:
            print("Failed to fetch data from the URL:", response)
    else:
        print("'input.txt' already exists. Skipping cookie check and request.")


def import_file_single_new_line(input_filename):
    with open(input_filename, 'r') as input_file:
        input = [line for line in input_file.read().split("\n") if line.strip()]
    return input


def import_file_double_new_line(input_filename):
    with open(input_filename, 'r') as input_file:
        input = [line for line in input_file.read().split("\n\n") if line.strip()]
    return input


def import_file_two_sections_double_new_line_separator(input_filename):
    '''
    Imports a file with two sections separated by a double new line.
    Returns two lists of strings, one for each section.

    expects input like:
    ```
    1-3
    2-10

    2
    5
    8
    ```
    '''
    with open(input_filename, 'r') as input_file:
        input = [line for line in input_file.read().split("\n\n") if line.strip()]

    part1 = input[0].split("\n")
    part2 = input[1].split("\n")
    if part2[-1] == '':
        part2 = part2[:-1]
    return part1, part2


def import_file_as_grid(input_filename, separator=None):
    input_grid=[]

    with open(input_filename, 'r') as input_file:
        input = [line for line in input_file.read().split("\n") if line.strip()]

    for line in input:
        if separator == ' ':
            input_grid.append(line.split())
        elif separator:
            input_grid.append(line.split(separator))
        else:
            input_grid.append([*line])

    return input_grid


def import_file_as_preformatted_grid(input_filename):
    '''
    Imports a file where columns are aligned by position, not delimiters.
    Preserves column alignment by detecting column positions from the data.

    Example input:
    ```
    123 328  51 64 
     45 64  387 23 
      6 98  215 314
    *   +   *   +  
    ```
    Returns cells with padding preserved as strings
    '''
    with open(input_filename, 'r') as input_file:
        lines = input_file.read().split("\n")
        # Remove trailing empty lines but keep lines with only whitespace
        while lines and not lines[-1].strip():
            lines.pop()

    if not lines:
        return []

    # Pad all lines to same length
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    # Find positions that are spaces in ALL rows - these are column separators
    separator_positions = []
    for pos in range(max_len):
        if all(line[pos] == ' ' for line in lines):
            separator_positions.append(pos)

    # Convert separator positions into column ranges
    col_ranges = []
    start = 0
    in_separator = separator_positions and separator_positions[0] == 0

    for pos in range(max_len):
        is_separator = pos in separator_positions

        if not in_separator and is_separator:
            # End of a column
            col_ranges.append((start, pos))
            in_separator = True
        elif in_separator and not is_separator:
            # Start of a new column
            start = pos
            in_separator = False

    # Don't forget the last column if it doesn't end with separator 🤦‍♂️
    if not in_separator:
        col_ranges.append((start, max_len))

    # Extract columns based on ranges
    grid = []
    for line in lines:
        row = []
        for start, end in col_ranges:
            cell = line[start:end].rstrip() # Remove trailing spaces only
            row.append(cell)
        grid.append(row)

    return grid


def product(lst):
    p = 1

    for i in list(map(int, lst)):
        p *= i

    return p


def three_part_parse_dict(input, first_delim, second_delim):
    '''
        parse lines like 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
    '''
    output={}

    for i in input:
        part_a, tmp = i.split(first_delim)
        part_b, part_c = tmp.split(second_delim)
        output[part_a] = [part_b.split(), part_c.split()]

    return output


def import_two_part_input(input, first_part_delim=",", second_part_delim=","):
    '''
    Where the input is split in to two sections like this, seperated by a double space, each with its own deliminator.
    `
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
    `
    Returns two lists
    '''

    part1, part2 = import_file_double_new_line(input)

    part1=[x.split(first_part_delim) for x in part1.split('\n')]
    part2 = [x.split(second_part_delim) for x in part2.split('\n')]
    return part1, part2


def convert_list_of_lists_to_ints(list:list):
    '''
    Convert a list of lists of strings to a list of lists of integers. I forget how to do this quickly ever year.
    '''
    return [[int(item) for item in sublist] for sublist in list]
