"""
task summary/notes
""" 

import fileinput
import collections

puzzle_input = list(fileinput.input('input.txt'))


def part1(puzzle_input):
    '''
            G - H       J - K - L
           /           /
    COM - B - C - D - E - F
                \
                 I
    '''

    orbits = collections.defaultdict(set)

    for line in puzzle_input:
        parent, child = line.rstrip().split(')')
        orbits[parent].add(child)

    checksums = {}

    def checksum(parent):
        if parent not in checksums:
            checksums[parent] = sum(checksum(child) + 1 for child in orbits.get(parent,()))
        return checksums[parent]


    return sum(map(checksum, orbits))




def part2():
    return "part 2"


print(part1(puzzle_input))
print(part2())