# pylint: disable-all
'''
# Import the shared functions
import sys
sys.path.append("../")
from shared import aoc_algorithms
'''

from collections import defaultdict, deque


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
