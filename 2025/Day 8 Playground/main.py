# pylint: disable-all
# Import AOC Common
import os
import sys
import time
sys.path.append("../")
from shared import aoc_common #, aoc_algorithms, aoc_grid_tools


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def calc_euclid_dist(a, b):
    # Calculate Euclidean distance in a cube.
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2


def calculate_distances(input):
    # find distances between each rown and the rows after it, then sort them.
    dists = []
    for ri, row in enumerate(input):
        for x in range(ri+1, len(input)):
            dists.append([calc_euclid_dist(row, input[x]), ri, x])
    dists.sort()
    return dists


def build_graph(edges, num_nodes):
    # Build list graph from list of edges
    graph = {i: [] for i in range(num_nodes)}
    for node_x, node_y, node_z in edges:
        graph[node_y].append(node_z)
        graph[node_z].append(node_y)
    return graph


def dfs(graph, nodes, elements, visited:set):
    # Depth-first search (DFS) to find connected elements in a graph
    visited.add(nodes)
    elements.append(nodes)

    for n in graph[nodes]:
        if n not in visited:
            dfs(graph, n, elements, visited)


def find_connected_elements(graph):
    # Find all connected components in a graph using Depth First Search (DFS)
    connected_elements = []
    visited = set()

    for node in graph:
        if node not in visited:
            elements = []
            dfs(graph, node, elements, visited)
            connected_elements.append(elements)

    return connected_elements


def part1(input):
    dists = calculate_distances(input)

    connections = 1000 if USE_REAL_DATA else 10
    p_graph = build_graph(dists[:connections], len(input))

    connected_elements = find_connected_elements(p_graph)
    length_of_nets = sorted([len(c) for c in connected_elements], reverse=True)

    return aoc_common.product(length_of_nets[:3])


def part2(input):
    dists = calculate_distances(input)
    p_graph = build_graph([], len(input))

    connection_idx = 0
    while True:
        node_x, node_y, node_z = dists[connection_idx]
        p_graph[node_y].append(node_z)
        p_graph[node_z].append(node_y)

        connected_elements = find_connected_elements(p_graph)

        # if there is only 1 element, thats the one
        if len(connected_elements) == 1:
            return input[node_y][0] * input[node_z][0]

        connection_idx += 1


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = [list(map(int,x.split(','))) for x in parsed_input]

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2}  ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
