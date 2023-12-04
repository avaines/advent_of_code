'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_common
'''

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
