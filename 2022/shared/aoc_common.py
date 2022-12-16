'''
# Import the shared functions
import sys
sys.path.append("../shared")
import aoc_common
'''

# from shared.common import generate_grid
def generate_grid(width, height, char=""):
    return [[char]*width for _ in range(height)]

def import_file_single_new_line(input_filename):
    with open(input_filename, 'r') as input_file:
        input = input_file.read().split("\n")
    return input

def import_file_double_new_line(input_filename):
    with open(input_filename, 'r') as input_file:
        input = input_file.read().split("\n")
    return input
