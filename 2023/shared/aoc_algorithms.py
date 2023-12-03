'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_algorithms

'''

def generate_grid(width, height, char=" "):
    return [[char]*width for _ in range(height)]



'''
Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree like data structures.
BFS can be easily implemented using recursion and data structures like dictionaries and lists.
'''
def breadth_first_search_grid(grid=[], start_coord=(0,0), wall="#", goal="*"):
    from collections import deque
    '''
        grid = [
            "..........",
            "..*#...##.",
            "..##...#*.",
            ".....###..",
            "......*..."
        ]
        breadth_first_search_grid(grid=grid, start_coord=(0,0))
    '''
    height = len(grid)
    width = len(list(grid[0]))

    queue = deque([[start_coord]])
    seen = set([start_coord])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def breadth_first_search_graph(graph = {}, starting_node=""):
    '''
        graph = {
            'A' : ['B','C'],
            'B' : ['D', 'E'],
            'C' : ['F'],
            'D' : [],
            'E' : ['F'],
            'F' : []
        }

        breadth_first_search_graph(graph, 'A')
    '''
    visited = [starting_node]
    queue   = [starting_node]

    while queue:
        s = queue.pop(0)
        print (s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

        return visited

