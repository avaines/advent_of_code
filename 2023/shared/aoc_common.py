'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_common
'''
import os
import requests
import regex


COOKIE_CACHE = "../../COOKIE"


def get_aoc_puzzle_data():
    ''' Get the puzzle data for a given puzzle using the cookie
       either enter it on each run or set the ENV VAR AOC_COOKIE '''
    path_extract = regex.search(r'/(\d{4})/Day (\d+).*', os.path.dirname(__file__))

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
        input = input_file.read().split("\n")
    return input


def import_file_double_new_line(input_filename):
    with open(input_filename, 'r') as input_file:
        input = input_file.read().split("\n\n")
    return input


def import_file_as_grid(input_filename):
    input_grid=[]

    with open(input_filename, 'r') as input_file:
        input = input_file.read().split("\n")

    for line in input:
        input_grid.append([*line])

    return input_grid


def product(lst):
    p = 1

    for i in list(map(int, lst)):
        p *= i

    return p


def three_part_parse_dict(input, first_delim, second_delim):
    output={}

    for i in input:
        part_a, tmp = i.split(first_delim)
        part_b, part_c = tmp.split(second_delim)
        output[part_a] = [part_b.split(), part_c.split()]

    return output
