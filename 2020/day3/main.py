"""
task summary/notes
"""

import fileinput
import collections

def part1(puzzle_input):
    pos_x = 0 # _
    pos_y = 0 # |
    tree_count = 0

    cur_y_row = 0
    while(pos_y < len(puzzle_input) ):

        for col in range(len(puzzle_input[pos_y])):
            #This position IS the x column of the current row
            if col == pos_x and cur_y_row == pos_y:
                if puzzle_input[pos_y][col] == "#":
                    #This postion is a tree at yx 
                    print("X", end='', sep='')
                    tree_count +=1
                else:
                    # This position is not a tree on the current row
                    print("O", end='', sep='')

            # This position is NOT the x column so just draw whatever is on the map
            else:
                print(puzzle_input[pos_y][col], end='', sep='')

        # Print a blank line
        print("")

        # Increment all the things
        pos_y +=1
        pos_x +=3
        cur_y_row +=1

        # If x is wider than then width of the map, strip the length of the visible display and start again
        # Hack to avoid drawing the map forever --->
        if pos_x >= len(puzzle_input[0]):
            pos_x = pos_x - len(puzzle_input[0])

    return tree_count



def part2(puzzle_input):

    return 0


# puzzle_input = list(fileinput.input('sample1.txt'))
with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input)
p2 = part2(puzzle_input)

print("#############################################################")
print("Part1: ", p1 )
print("Part2: ", p2 )