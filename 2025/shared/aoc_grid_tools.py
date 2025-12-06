# pylint: disable-all
'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_grid_tools
'''
import os
import time


# Output and Transformation Tools

def generate_grid(width, height, char=" "):
    return [[char]*width for _ in range(height)]


def draw_grid_to_console(grid: list[list[any]], headerText="", delay=0.1, clear=True):
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    if headerText:
        print(headerText)

    for row in grid:
        row = [str(i) for i in row]
        print(''.join(row))
    time.sleep(delay)


def rotate_grid_90_clockwise(grid):
    ''' Rotates a grid 90 degrees clockwise '''
    return [list(reversed(col)) for col in zip(*grid)]


def rotate_grid_90_anticlockwise(grid):
    ''' Rotates a grid 90 degrees anticlockwise '''
    return [list(col) for col in zip(*grid)]


# Searching and Navigation Tools

def find_coords_of_char_in_grid(grid: list[list[any]], char):
    return [(ri, ci) for ri, row in enumerate(grid) for ci, cell in enumerate(row) if cell == char]


def get_all_grid_neighbours(row, column, grid, diagonals=False):
    '''
    Get all valid neighboring coordinates in a grid.
    Args:
        row (int): The row index of the current position.
        column (int): The column index of the current position.
        grid (list of list): The grid to check against.
        diagonals (bool): Whether to include diagonal neighbors.
    Returns:
        list of tuple: A list of valid neighboring coordinates.
    '''
    neighborIndexes = []
    neighborVals = []
    neighbors = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonals:
        directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for drow, dcol in directions:
        nrow, ncol = row + drow, column + dcol
        if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
            neighborIndexes.append((nrow, ncol))
            neighborVals.append(grid[nrow][ncol])
            neighbors[(nrow, ncol)] = grid[nrow][ncol]
    return {"indexes": neighborIndexes, "values": neighborVals, "dict": neighbors}


def grid_word_search(grid:list[list], word:str, vertical=True, horizontal=True, diagonal=True):
    ''' function to find the word XMAS in a 'grid' like this:
        [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
        ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
        ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
        ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
        ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
        ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
        ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
        ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
        ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
        ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
    '''
    word_length=len(word)
    instances_of_word=[]

    directions = []
    if horizontal: directions.append((0, 1))  # right
    if horizontal: directions.append((0, -1)) # left
    if vertical: directions.append((1, 0))    # down
    if vertical: directions.append((-1, 0))   # up
    if diagonal: directions.append((1, 1))    # down-right
    if diagonal: directions.append((1, -1))   # down-left
    if diagonal: directions.append((-1, 1))   # up-right
    if diagonal: directions.append((-1, -1))  # up-left

    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    for r, row in enumerate(grid):
        for c, column in enumerate(row):
            if grid[r][c] == word[0]:  # Match the first letter of the word
                for dr, dc in directions:  # Explore all 8 directions
                    match_coords = []
                    for i in range(word_length):
                        nr, nc = r + dr * i, c + dc * i
                        if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                            break
                        match_coords.append((nr, nc))
                    if len(match_coords) == word_length:  # Full match found
                        instances_of_word.append(match_coords)

    return instances_of_word

def breadth_first_search_grid(grid=[], start_coord=(0,0), wall="#", goal="*"):
    '''
    Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree like data structures.
    BFS can be easily implemented using recursion and data structures like dictionaries and lists.

    grid = [
        "..........",
        "..*#...##.",
        "..##...#*.",
        ".....###..",
        "......*..."
    ]
    breadth_first_search_grid(grid=grid, start_coord=(0,0))
    '''
    from collections import deque
    height = len(grid)
    width = len(grid[0])

    queue = deque([start_coord])
    seen = set(start_coord)

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


# Validation Tools

def is_in_bounds_of_grid(grid: list[list[any]], coords: tuple[int,int]):
    if 0 <= coords[0] < len(grid): # Check Rows
        if 0 <= coords[1] < len(grid[0]): # Check first columns in first row
            return True
    return False

