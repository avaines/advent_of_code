# pylint: disable-all
'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_algorithms
'''

from collections import defaultdict, deque


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


def topological_sort_khans(items:list, node_rules:map):
    '''
    Kahn's Topological sort algorithm: 
        - https://en.wikipedia.org/wiki/Topological_sorting#Kahn
        - https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
    
       items = [1, 2, 3, 4, 5, 6]
       node_rules = {1:[2, 3], 2:[4], 3:[4,5], 4:[6], 5:[6], 6:[]}
       topological_sort_khans(items, node_rules) -> will return '[1, 2, 3, 4, 5, 6]'

       items2 = ["build","test","deploy","design","code"]
       node_rules2 = {"design": ["code"], "code": ["build"], "build": ["test"], "test": ["deploy"], "deploy": []}
       topological_sort_khans(items2, node_rules2) - will return '["design", "code", "build", "test", "deploy"]'
    '''

    adj = defaultdict(list)
    in_degree = {item: 0 for item in items}

    for before in node_rules:
        if before in items:
            for after in node_rules[before]:
                if after in items:
                    adj[before].append(after)
                    in_degree[after] += 1

    queue = deque([item for item in items if in_degree[item] == 0])
    result = []

    while queue:
        item = queue.popleft()
        result.append(item)

        for neighbor in adj[item]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(items) else None