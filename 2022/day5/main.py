import os

INPUT_DEBUG = True
P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

class Crane():
    def __init__(self, crate_map_raw):
        self.crate_map = self.process_crate_stacks(crate_map_raw)

    def process_crate_stacks(self,stack_data):
        # from the input which is over multiple lines (now a list for each text row)
        # which contains all the extra spacing and [ ] characters, loop through it, and return just a positional
        # list which contains a 'cell' for each crate with its letter or a blank entry
        parent_list = []
        for text_row in stack_data[0:-1]:
            reader_head_pointer_index = 1 # start at 1 to skip the first item
            child_list = []

            while reader_head_pointer_index <= len(text_row):
                child_list.append(text_row[reader_head_pointer_index])
                reader_head_pointer_index += 4

            # This would just include the extra padding
            parent_list.append(child_list)

        # I suspect a vertically arranged list of lists wont work as when it stacks a crate on top of the highest crate it will break
        # so transpose the list of lists to a dict where each crate ID is a list of the crates in order
        total_number_of_stacks = (stack_data[-1].split())[-1]
        crate_map = dict()
        for stack_id in range(int(total_number_of_stacks)):
            crate_map[stack_id +1] = []
            for stack_row in parent_list:
                # for crate_position in range(len(stack_row)):
                crate_map[stack_id +1].append(stack_row[stack_id])

            # remove the padding from the list of stacked crates
            crate_map[stack_id +1] = [x for x in crate_map[stack_id +1] if x != ' ']

            # reverse so that the 'top' most item is now at -1 for the list. bottom is now 0
            crate_map[stack_id +1].reverse()

        return crate_map

    # CrateMover 9000 mode
    def move_crate_by_crate(self, DEBUG, instruction):
        instruction_breakdown = instruction.split()
        inst_moves = int(instruction_breakdown[1])
        inst_from = int(instruction_breakdown[3])
        inst_to = int(instruction_breakdown[5])

        for move in range(inst_moves):
            if DEBUG: print("moving", self.crate_map[inst_from][-1], "from stack", inst_from , "to stack", inst_to)
            self.crate_map[inst_to].append(self.crate_map[inst_from].pop())

    # CrateMover 9001 mode
    def move_crates_by_stack(self, DEBUG, instruction):
        instruction_breakdown = instruction.split()
        inst_moves = int(instruction_breakdown[1])
        inst_from = int(instruction_breakdown[3])
        inst_to = int(instruction_breakdown[5])

        if DEBUG: print("moving", self.crate_map[inst_from][-inst_moves:], "from stack", inst_from , "to stack", inst_to)

        crane_grabber = self.crate_map[inst_from][-inst_moves:]

        del self.crate_map[inst_from][len(self.crate_map[inst_from]) -inst_moves:]

        self.crate_map[inst_to] += crane_grabber

    def top_most_crates(self,DEBUG):
        top_most_crates = ""
        for stack in self.crate_map:
            if DEBUG: print("Top crate in stack",stack, "is", self.crate_map[stack][-1])
            top_most_crates += self.crate_map[stack][-1]
        return top_most_crates

def input_parser(input):
    # Logic moved to Class due to variable persitence 
    return input[0].split("\n"), input[1].split("\n")

def part1(crate_map, instructions):
    crane_9000 = Crane(crate_map)

    for instruction in instructions:
        if P1_DEBUG: print("Next instruction:", instruction )
        crane_9000.move_crate_by_crate(P1_DEBUG, instruction)

    return crane_9000.top_most_crates(P1_DEBUG)

def part2(crate_map, instructions):
    crane_9001 = Crane(crate_map)

    for instruction in instructions:
        if P2_DEBUG: print("Next instruction:", instruction )
        crane_9001.move_crates_by_stack(P2_DEBUG, instruction)

    return crane_9001.top_most_crates(P2_DEBUG)


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        crate_map, instructions = input_parser(input_file.read().split("\n\n"))

    print()
    print("# # # SOLUTIONS # # #")

    part_1 = part1(crate_map, instructions)
    print("Part1:", part_1 )
    print()

    part_2 = part2(crate_map, instructions)
    print("Part2:", part_2 )
6