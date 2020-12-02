"""
task summary/notes
"""

import fileinput
import collections
from operator import xor

def log(part, input):
    if p1_log and part == 1:
        print(input)

    if p2_log and part == 2:
        print(input)


def part1(puzzle_input):
    valid_pws_count = 0

    for row in puzzle_input:

        # 1-3 a: abcde
        # Split passwords down
        data = row.split(": ")
        password = data[1].strip() # trim whitespace
        meta = data[0].split(" ")
        boundaries = meta[0].split("-")
        req_char = meta[1]

        log(1, password + " requires between " + boundaries[0] + " and " + boundaries[1] + " " + req_char)

        if password.count(req_char) >= int(boundaries[0]) and password.count(req_char) <= int(boundaries[1]):
            log(1, password + " is ok")
            valid_pws_count += 1

    return valid_pws_count


def part2(puzzle_input):

    valid_pws_count = 0

    for row in puzzle_input:

        # 1-3 a: abcde
        # Split passwords down
        data = row.split(": ")
        password = data[1].strip() # trim whitespace
        meta = data[0].split(" ")
        boundaries = meta[0].split("-")
        req_char = meta[1]

        if xor(password[int(boundaries[0])-1] == req_char, password[int(boundaries[1])-1] == req_char):
            print("GOOD", password,password[int(boundaries[0])-1],int(boundaries[0]),"=", req_char, ", or is",password[int(boundaries[1])-1],int(boundaries[1]),"=", req_char)
            log(2, password + " is ok")
            valid_pws_count += 1

        else:
            print("BAD", password,password[int(boundaries[0])-1],int(boundaries[0]),"=", req_char, ", or is",password[int(boundaries[1])-1],int(boundaries[1]),"=", req_char)

    return valid_pws_count


p1_log = False
p2_log = True

# puzzle_input = list(fileinput.input('sample1.txt'))
with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input)
p2 = part2(puzzle_input)

print("#############################################################")
print("Part1: ", p1 )
print("Part2: ", p2 )