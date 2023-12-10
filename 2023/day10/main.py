
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


def part1(input):
    # Find the starting coords
    for row_i, row in enumerate([*input]):
        if 'S' in row:
            if P1_DEBUG: print(f"Starting postition found; row {row_i}, column {row.index("S")}")
            position = (row.index("S"), row_i)
            break

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

    return max(positions_visited.values())


def part2(input):
    if P2_DEBUG: print(f"Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_as_grid(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
