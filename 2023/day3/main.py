
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import collections

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

class engine():
    def __init__(self, schematic):
        self.schematic = schematic
        self.parts_seen=[]
        self.parts_with_adjacent_symbols=[]
        self.gear_adjacent_parts = collections.defaultdict(list)

    def has_adjacent_symbol(self, row_i, column_i):
        def is_symbol(char):
            if char.isalpha() or char.isdigit() or char == '.':
                return False
            else:
                return True

        # Check above
        if row_i > 0:
            if is_symbol(self.schematic[row_i -1][column_i]):
                return [row_i -1, column_i]

        # Check below
        if row_i < len(self.schematic)-1:
            if is_symbol(self.schematic[row_i +1][column_i]):
                return [row_i +1, column_i]

        # Check left
        if column_i > 0:
            if is_symbol(self.schematic[row_i][column_i -1]):
                return [row_i, column_i -1]

        # Check right
        if column_i < len(self.schematic[0]) -1:
            if is_symbol(self.schematic[row_i][column_i +1]):
                return [row_i, column_i +1]

        # Check above right
        if row_i > 0 and column_i < len(self.schematic[0]) -1:
            if is_symbol(self.schematic[row_i -1][column_i +1]):
                return [row_i -1, column_i+1]

        # Check above left
        if row_i > 0 and column_i > 0:
            if is_symbol(self.schematic[row_i -1][column_i -1]):
                return [row_i -1, column_i -1]

        # Check below right
        if row_i < len(self.schematic) -1 and column_i < len(self.schematic[0]) -1:
            if is_symbol(self.schematic[row_i +1][column_i +1]):
                return [row_i +1, column_i +1]

        # Check below left
        if row_i < len(self.schematic) -1 and column_i > 0:
            if is_symbol(self.schematic[row_i +1][column_i -1]):
                return [row_i +1, column_i -1]

        return None

    def calculate_part_numbers(self):
        for ri, row in enumerate(self.schematic):
            this_int = []
            part_has_ajacency = False

            gear_adjacent_found_for_part = None
            for ci, column in enumerate(row):

                if column.isdigit():
                    this_int.append(column)
                    adjacent_part_location = self.has_adjacent_symbol(ri, ci)
                    if adjacent_part_location != None:
                        if P1_DEBUG: print(f"row {ri}, column {ci} ({self.schematic[ri][ci]}) has a part adjacent at {adjacent_part_location}, its a {self.schematic[adjacent_part_location[0]][adjacent_part_location[1]]}")
                        part_has_ajacency=True

                        if self.schematic[adjacent_part_location[0]][adjacent_part_location[1]] == "*":
                            gear_adjacent_found_for_part = adjacent_part_location

                if not column.isdigit() or ci == len(row) -1:
                    if len(this_int)>0 and part_has_ajacency:
                        self.parts_with_adjacent_symbols.append("".join(this_int))
                        part_has_ajacency = False

                        if gear_adjacent_found_for_part != None:
                            self.gear_adjacent_parts[f"{gear_adjacent_found_for_part}"].append("".join(this_int))
                        gear_adjacent_found_for_part = None

                    if len(this_int)>0:
                        self.parts_seen.append("".join(this_int))
                        this_int=[]

def part1():
    return sum(list(map(int, ENGINE.parts_with_adjacent_symbols)))

def part2():
    gear_ratio = 0
    for gear in ENGINE.gear_adjacent_parts:
        gear_parts = ENGINE.gear_adjacent_parts[gear]
        if len(gear_parts) >= 2:
            gear_ratio += aoc_common.product(gear_parts)

    return gear_ratio


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    ENGINE = engine(parsed_input)
    ENGINE.calculate_part_numbers()

    part_1 = part1()
    part_2 = part2()

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
