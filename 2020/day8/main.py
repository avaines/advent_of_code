"""
Day 8: Handheld Halting
"""
import fileinput
import collections
class assembler_state():
    # Seperation of conserns.
    # This is a state of the computer, think VM memory
    def __init__(self, assembler_code, debug):
        if debug:print("Assembler state initialised...")
        self.debug = debug

        #Break the lines up with list comprehension rather than a set of for loops
        self.assembler_code = assembler_code
        self.accumulator = 0
        self.visited = [False for x in self.assembler_code]
        self.pointer = 0

class assembler_executor():
    # This will now take a 'state' as  parameter to allow multiple computers
    def execute(self, state):
        # loop through a list from 0 to length of the input/code as long as
        # the current pointer isnt in the list of visited operations
        while (0 <= state.pointer < len(state.assembler_code) and (not state.visited[state.pointer])):

            #Get current operation at the pointer
            instruction, argument = operation = state.assembler_code[state.pointer]
            if state.debug:print("Current operation:",state.pointer, operation)

            #Mark this operation as visited
            state.visited[state.pointer] = True

            if instruction == "nop":
                state.pointer +=1
                continue

            if instruction == "acc":
                state.accumulator += int(argument)
                state.pointer += 1

            if instruction == "jmp":
                state.pointer += int(argument)

            if state.pointer >= len(state.assembler_code):
                if state.debug:print("Executor has execute after:", state.pointer, operation)
                return 99999999, state.accumulator

        return 0, state.accumulator


def part1(input, debug):
    #Break the lines up with list comprehension rather than a set of for loops
    code = [tuple(line.split(" ")) for line in input]
    state = assembler_state(code, debug)

    return games_console.execute(state)[1]

def part2(input, debug):
    code = [tuple(line.split(" ")) for line in input]

    for i in range(0, len(code)):

        if code[i][0] == "nop":
            code[i] = ("jmp", code[i][1])
        elif code[i][0] == "jmp":
            code[i] = ("nop", code[i][1])

        # Create a new memory state using these changes
        state = assembler_state(code, debug)
        game_console_result = games_console.execute(state)

        if game_console_result[0] == 99999999:
            if debug: print("Found the result by changing instruction at line: ", i )
            return game_console_result[1]

        # Reset things and go again
        code = [tuple(line.split(" ")) for line in input]
        i +=1

    return 0


with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

games_console = assembler_executor()
p1 = part1(puzzle_input, False)
p2 = part2(puzzle_input, False)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )
