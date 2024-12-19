import os

INPUT_DEBUG = True
P1_DEBUG    = False
P2_DEBUG    = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def is_tree_visible(debug, grid, x, y):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    grid_height = len(grid)
    grid_width = len(grid[0])

    # For each of the possible directions a tree can be assessed from (up, down, left, right)
    for direction_x, direction_y in directions:
        check_x = x + direction_x
        check_y = y + direction_y

        # while the current check coordinate is within the height boundry, AND the tree in the direction we are checking is lower than the target tree
        # increment the check counters by the current direction loop
        while 0 <= check_x < grid_height and 0 <= check_y < grid_width and grid[check_x][check_y] < grid[x][y]:
            check_x += direction_x
            check_y += direction_y

        # If the tree is visible, abort the checking and just return True, as if we see it from any direction its game over
        if not (0 <= check_x < grid_height and 0 <= check_y < grid_width):
            if debug: print("The tree at %sx%s, a %s, is visible" %(x,y,grid[x][y]))
            return True

    # If we didn't exit True earlier, that means the tree is hidden
    if debug: print("The tree at %sx%s, a %s, is hidden" %(x,y,grid[x][y]))
    return False

def tree_senic_score(debug, grid, x, y):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    grid_height = len(grid)
    grid_width = len(grid[0])
    current_score = 1

    # For each of the possible directions a tree can be assessed from (up, down, left, right)
    for direction_x, direction_y in directions:
        current_direction_score = 0
        check_x = x + direction_x
        check_y = y + direction_y

        # while the current check coordinate is within the height boundry, AND the width boundry
        # increment the check counters by the current direction loop
        while 0 <= check_x < grid_height and 0 <= check_y < grid_width:
            current_direction_score += 1

            # If the tree in the direction being checked is bigger than target treee end this check
            if grid[check_x][check_y] >= grid[x][y]:
                break

            check_x += direction_x
            check_y += direction_y

        current_score *= current_direction_score

    if debug: print("The tree at %sx%s, a %s, has a viewing score of %s" %(x, y, grid[x][y], current_score))
    return current_score

def input_parser(input):
    grid = []
    for row in input:
        # convert the row of ints to a list of individual integers using map
        grid.append(list(map(int,list(row))))

    return grid

def part1(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    visible_trees = 0

    # Loop through each x position in all rows of the grid
    for x_coord in range(grid_height):
        for y_coord in range(grid_width):
            # This too many nested loops was confusing, moved to function
            if is_tree_visible(P1_DEBUG, grid, x_coord, y_coord):
                visible_trees += 1

    return visible_trees

def part2(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    best_scenic_score = 0

    # Loop through each x position in all rows of the grid
    for x_coord in range(grid_height):
        for y_coord in range(grid_width):
            best_scenic_score = max(best_scenic_score, tree_senic_score(P2_DEBUG, grid, x_coord, y_coord))

    return best_scenic_score


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )