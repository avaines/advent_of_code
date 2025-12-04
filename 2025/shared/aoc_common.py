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


def import_file_as_grid(input_filename):
    input_grid=[]

    with open(input_filename, 'r') as input_file:
        input = [line for line in input_file.read().split("\n") if line.strip()]

    for line in input:
        input_grid.append([*line])

    return input_grid


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


def draw_grid_to_console(grid: list[list[any]], headerText="", delay=0.1, clear=True):
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    if headerText:
        print(headerText)

    for row in grid:
        row = [str(i) for i in row]
        print(''.join(row))
    time.sleep(delay)


def is_in_bounds_of_grid(grid: list[list[any]], coords: tuple[int,int]):
    if 0 <= coords[0] < len(grid): # Check Rows
        if 0 <= coords[1] < len(grid[0]): # Check first columns in first row
            return True
    return False

def find_coords_of_char_in_grid(grid: list[list[any]], char):
    return [(ri, ci) for ri, row in enumerate(grid) for ci, cell in enumerate(row) if cell == char]
