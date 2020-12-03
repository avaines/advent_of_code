"""
task summary/notes
"""

import fileinput
import collections

def part1(puzzle_input, draw):

    return slope_master(puzzle_input, 3, 1, draw)


def slope_master(puzzle_input, route_right, route_down, draw):
    pos_x = 0 # _
    pos_y = 0 # |
    tree_count = 0
    route_down_check = route_down

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
        if route_down_check == 1:
            pos_y += route_down
            pos_x += route_right
            route_down_check = route_down
        else:
            route_down_check = route_down_check-1

        cur_y_row +=1

        # If x is wider than then width of the map, strip the length of the visible display and start again
        # Hack to avoid drawing the map forever --->
        if pos_x >= len(puzzle_input[0]):
            pos_x = pos_x - len(puzzle_input[0])

    return tree_count


def part2(puzzle_input, draw):
    # List of routes (right, down)
    routes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    tree_count_product = 1

    for route in routes:
        print("Right: ", route[0], ", Down: ", route[1])
        tree_count_product = tree_count_product * slope_master(puzzle_input, route[0], route[1], draw)

    return tree_count_product


# puzzle_input = list(fileinput.input('sample1.txt'))
with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input, False)
p2 = part2(puzzle_input, False)

print("#############################################################")
print("Part1: ", p1 )
print("Part2: ", p2 )