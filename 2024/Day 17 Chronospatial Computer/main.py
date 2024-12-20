# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = False
P2_DEBUG = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample6.txt" % os.path.dirname(os.path.realpath(__file__))


class intcode_computer:
    def __init__(self, register_a, register_b, register_c, program):
        self.reg_a = register_a
        self.reg_b = register_b
        self.reg_c = register_c
        self.program = program
        self.instruction_pointer = 0
        self.output_buffer = []
        self.finished = False


    def reset(self, register_a=None, register_b=None, register_c=None, program=None):
        if register_a is not None: self.reg_a = register_a
        if register_b is not None: self.reg_b = register_b
        if register_c is not None: self.reg_c = register_c
        if program is not None: self.program = program
        self.instruction_pointer = 0
        self.output_buffer = []
        self.finished = False


    def combo(self, operand):
        # Combo operands 0 through 3 represent literal values 0 through 3.
        # Combo operand 4 represents the value of register A.
        # Combo operand 5 represents the value of register B.
        # Combo operand 6 represents the value of register C.
        # Combo operand 7 is reserved and will not appear in valid programs.
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.reg_a
            case 5:
                return self.reg_b
            case 6:
                return self.reg_c
            case _:
                return False

    def inst_adv(self, operand):
        # The adv instruction (opcode 0) performs division.
        # The numerator is the value in the A register.
        # The denominator is found by raising 2 to the power of the instruction's combo operand.
        # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
        # The result of the division operation is truncated to an integer and then written to the A register.
        denominator = 2**self.combo(operand)
        adv = self.reg_a//denominator
        if P1_DEBUG: print(f" Opcode 0: {self.reg_a}//{denominator}={adv}")
        self.reg_a = adv

    def inst_bxl(self, operand):
        # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand,
        # then stores the result in register B.
        bxl = self.reg_b ^ operand
        if P1_DEBUG: print(f" Opcode 1: XOR {self.reg_b}/{operand} = {bxl}")
        self.reg_b = bxl

    def inst_bst(self, operand):
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits),
        # then writes that value to the B register.
        combo = self.combo(operand)
        bst = combo%8
        if P1_DEBUG: print(f" Opcode 2: combo {operand} is {combo}; mod 8 is {bst}")
        self.reg_b = self.combo(operand)%8

    def inst_jnz(self, operand):
        # The jnz instruction (opcode 3) does nothing if the A register is 0.
        # However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
        # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        if self.reg_a != 0:
            if P1_DEBUG: print(f" Opcode 3: Jumping pointer to {operand}")
            self.instruction_pointer = operand
        else:
            self.instruction_pointer +=2

    def inst_bxc(self, operand):
        # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. 
        # (For legacy reasons, this instruction reads an operand but ignores it.)
        bxc = self.reg_b ^ self.reg_c
        if P1_DEBUG: print(f" Opcode 4: Bitwise {self.reg_b} and /{self.reg_c} is {bxc}")
        self.reg_b = bxc

    def inst_out(self, operand):
        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8 then outputs that value.
        # (If a program outputs multiple values, they are separated by commas.)
        combo = self.combo(operand)
        out = combo % 8
        self.reg_b = out
        self.output_buffer.append(out)
        if P1_DEBUG: print(f" Opcode 5: Combo of {operand} is {combo}; mod 8 is {out}. Added to output buffer")

    def inst_bdv(self, operand):
        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register.
        denominator = 2**self.combo(operand)
        bdv = self.reg_a//denominator
        if P1_DEBUG: print(f" Opcode 0: {self.reg_a}/{denominator}={bdv}")
        self.reg_b = bdv

    def inst_cdv(self, operand):
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register.
        denominator = 2**self.combo(operand)
        cdv = self.reg_a//denominator
        if P1_DEBUG: print(f" Opcode 0: {self.reg_a}/{denominator}={cdv}")
        self.reg_c = cdv

    def draw(self):
        pointer_pos_buffer=[" "]*self.instruction_pointer

        pointer_pos_buffer.append(f"^| \t :{self.output_buffer}")
        aoc_common.draw_grid_to_console(
            [
                self.program,
                pointer_pos_buffer,
                f"A-{self.reg_a},B-{self.reg_b}, C-{self.reg_c}"
            ],0.1,False)
        print()

    def compute(self):
        if self.instruction_pointer<=len(self.program)-1:

            this_opcode = self.program[self.instruction_pointer]
            this_operand = self.program[self.instruction_pointer+1]

            match this_opcode:
                case 0:
                    self.inst_adv(this_operand)
                case 1:
                    self.inst_bxl(this_operand)
                case 2:
                    self.inst_bst(this_operand)
                case 3:
                    self.inst_jnz(this_operand)
                case 4:
                    self.inst_bxc(this_operand)
                case 5:
                    self.inst_out(this_operand)
                case 6:
                    self.inst_bdv(this_operand)
                case 7:
                    self.inst_cdv(this_operand)

            if this_opcode not in [3]:
                if self.instruction_pointer <= len(self.program)-2:
                    self.instruction_pointer += 2
                else:
                    self.finished = True

        else:
            self.finished = True


def part1(registers, program):
    reg_a = int(registers[0].split(": ")[1])
    reg_b = int(registers[1].split(": ")[1])
    reg_c = int(registers[2].split(": ")[1])
    program = list(program.split(": ")[1].split(","))
    program = [int(c) for c in program]

    computer = intcode_computer(reg_a, reg_b, reg_c, program)

    if P1_DEBUG: computer.draw()
    while not computer.finished:
        computer.compute()
        if P1_DEBUG: computer.draw()

    output = ",".join([str(o) for o in computer.output_buffer])
    if P1_DEBUG: print(f"Registers; A-{computer.reg_a}, B-{computer.reg_b}, C-{computer.reg_c}. Output {output}")
    return output


def part2(registers, program):
    reg_a = int(registers[0].split(": ")[1])
    reg_b = int(registers[1].split(": ")[1])
    reg_c = int(registers[2].split(": ")[1])
    program = list(program.split(": ")[1].split(","))
    program = [int(c) for c in program]
    computer = intcode_computer(reg_a, reg_b, reg_c, program)

    while computer.output_buffer != program:
        computer.reset(register_a=reg_a)
        while not computer.finished:
            computer.compute()
            if P2_DEBUG: computer.draw()
        reg_a += 1

    return reg_a


if __name__ == '__main__':
    parsed_registers, parsed_program = aoc_common.import_file_double_new_line (INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_registers = parsed_registers.split("\n")
    start_time_part1 = time.time()
    part_1 = part1(parsed_registers, parsed_program)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_registers, parsed_program)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
