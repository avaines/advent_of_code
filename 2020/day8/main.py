"""
Day 8: Handheld Halting
"""
import fileinput
import collections

import copy

class assembler():
    def __init__(self, puzzle_input_raw_lines, debug):
        if debug:print("Assembler initialising...")
        self.debug = debug

        #Break the lines up with list comprehension rather than a set of for loops
        self.assembler_code = [tuple(line.split(" ")) for line in puzzle_input_raw_lines]
        self.accumulator = 0
        self.visited = [False for x in self.assembler_code]
        self.pointer = 0

    def execute(self):
        # loop through a list from 0 to length of the input/code as long as
        # the current pointer isnt in the list of visited operations
        while (0 <= self.pointer < len(self.assembler_code) and (not self.visited[self.pointer])):

            #Get current operation at the pointer
            instruction, argument = operation = self.assembler_code[self.pointer]
            if self.debug:print("Current operation:",self.pointer, operation)

            #Mark this operation as visited
            self.visited[self.pointer] = True

            if instruction == "nop":
                self.pointer +=1
                continue

            if instruction == "acc":
                if argument[0]=="-": self.accumulator -= int(argument[1:])
                if argument[0]=="+": self.accumulator += int(argument[1:])
                self.pointer += 1

            if instruction == "jmp":
                if argument[0]=="-": self.pointer -= int(argument[1:])
                if argument[0]=="+": self.pointer += int(argument[1:])
                else:
                    if self.debug:print("Something went wrong with the JMP operation in", operation)

        return self.accumulator

def part1(input, debug):
    games_console = assembler(input, debug)
    return games_console.execute()

def part2(input, debug):
    return 0

with open('sample.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input, False)
p2 = part2(puzzle_input, False)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )