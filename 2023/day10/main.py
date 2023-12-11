
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


direction_map = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w")
}

move_map = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
    }

def find_start_s(grid):
    for row_i, row in enumerate([*grid]):
        if 'S' in row:
            if P1_DEBUG: print(f"Starting postition found; row {row_i}, column {row.index("S")}")
            return (row.index("S"), row_i)

def part1(input):
    position = find_start_s(input)

    positions_visited = dict()
    search_queue = [(position, 0)]

    while len(search_queue) > 0:
        current, distance = search_queue.pop(0)
        if P1_DEBUG: print(f"Starting at {current} which is a {input[current[0]][current[1]]}, ", end = '')

        if current in positions_visited:
            if P1_DEBUG: print(f", we've already visited this position")
            continue

        positions_visited[current] = distance
        y,x = current

        available_directions = move_map[input[y][x]]

        for direction in available_directions:
            dy, dx, opposite_direction = direction_map[direction]
            new = (y + dy, x + dx)

            if y + dy <0 or y + dy >=len(input):
                if P1_DEBUG: print(f", following would cause us to go out of bounds")
                continue
            if x + dx <0 or x + dx >= len(input[0]):
                if P1_DEBUG: print(f", following would cause us to go out of bounds")
                continue

            target = input[y+dy][x+dx]

            if target not in move_map:
                if target == '.':
                    if P1_DEBUG: print(f", target is a '.', skipping")
                else:
                    if P1_DEBUG: print(f", target is an illegal character, skipping")
                continue

            target_directions = move_map[target]

            if opposite_direction in target_directions:
                search_queue.append((new, distance+1))

        if P1_DEBUG: print(f", moving to {new} which is a {input[current[0]][current[1]]}")

    return max(positions_visited.values()), positions_visited


def part2(input, pipe_coords):
    fill_grid = aoc_algorithms.generate_grid(len(input[0]), len(input), 0)
    s_position = find_start_s(input)
    input[s_position[1]][s_position[0]] = "-"

    for pc in pipe_coords:
        fill_grid[pc[0]][pc[1]] = 1

    counter = 0
    for row_i, row in enumerate(input):
        inside = False
        for column_i, _ in enumerate(row):
            if fill_grid[row_i][column_i]:
                if input[row_i][column_i] in ["|", "J", "L"]:
                    inside = not inside
            else:
                counter += inside

    return counter


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input, part_1[1])

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1[0] )
    print("Part2:", part_2 )
