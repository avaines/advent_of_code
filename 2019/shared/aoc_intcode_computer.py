# pylint: disable-all
'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_algorithms
'''

# Used for Puzzle days 2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23
class initcode_computer:
    def __init__(self, program, input_values=[]):
        self.program = program.copy()
        self.input_values = input_values
        self.output_values = []
        self.pointer = 0
        self.halted = False


    def get_parameter(self, mode, value):
        if mode == 0:  # position mode
            return self.program[value]
        elif mode == 1:  # immediate mode
            return value
        else:
            raise ValueError(f"Unknown parameter mode: {mode}")


    def run(self):
        while not self.halted:
            instruction = str(self.program[self.pointer]).zfill(5)
            opcode = int(instruction[-2:])
            modes = list(map(int, instruction[:-2]))[::-1]

            if opcode == 1:  # addition
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                param2 = self.get_parameter(modes[1], self.program[self.pointer + 2])
                dest = self.program[self.pointer + 3]
                self.program[dest] = param1 + param2
                self.pointer += 4

            elif opcode == 2:  # multiplication
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                param2 = self.get_parameter(modes[1], self.program[self.pointer + 2])
                dest = self.program[self.pointer + 3]
                self.program[dest] = param1 * param2
                self.pointer += 4

            elif opcode == 3:  # input
                if not self.input_values:
                    raise ValueError("Input expected but no input values available.")
                dest = self.program[self.pointer + 1]
                self.program[dest] = self.input_values.pop(0)
                self.pointer += 2

            elif opcode == 4:  # output
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                self.output_values.append(param1)
                self.pointer += 2

            elif opcode == 5:  # jump-if-true
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                param2 = self.get_parameter(modes[1], self.program[self.pointer + 2])
                if param1 != 0:
                    self.pointer = param2
                else:
                    self.pointer += 3

            elif opcode == 6:  # jump-if-false
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                param2 = self.get_parameter(modes[1], self.program[self.pointer + 2])
                if param1 == 0:
                    self.pointer = param2
                else:
                    self.pointer += 3

            elif opcode == 7:  # less than
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                param2 = self.get_parameter(modes[1], self.program[self.pointer + 2])
                dest = self.program[self.pointer + 3]
                self.program[dest] = 1 if param1 < param2 else 0
                self.pointer += 4

            elif opcode == 8:  # equals
                param1 = self.get_parameter(modes[0], self.program[self.pointer + 1])
                param2 = self.get_parameter(modes[1], self.program[self.pointer + 2])
                dest = self.program[self.pointer + 3]
                self.program[dest] = 1 if param1 == param2 else 0
                self.pointer += 4

            

            elif opcode == 99:  # halt
                self.halted = True

            else:
                raise ValueError(f"Unknown opcode: {opcode}")
