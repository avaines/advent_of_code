"""
Day X: Title
"""
import fileinput
import itertools


def part1(puzzle_input, preamble, debug):

    for i in range (preamble, len(puzzle_input)):
        solution_found = False
        checksum = [ int(x) for x in puzzle_input[i - preamble : i] ]

        for combos in itertools.combinations(checksum, 2):
            if debug: print("current pointer is ",puzzle_input[i],"- current checksum is", combos)
            if sum(combos) == int(puzzle_input[i]):
                solution_found = True
                break

        if not solution_found:
            return int(puzzle_input[i])

    return 0


def part2(puzzle_input, bad_val, debug):
    for i in range(len(puzzle_input)):
        for l in range(i, len(puzzle_input)):
            checksum = [ int(x) for x in puzzle_input[i : l+1] ]

            if sum(checksum )== bad_val:
                return min(checksum) + max(checksum)

    return 0


with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

preamble = 25

p1 = part1(puzzle_input, preamble, False)
p2 = part2(puzzle_input, p1, True)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )