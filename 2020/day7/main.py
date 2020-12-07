"""
Day 7: Handy Haversacks
"""
import fileinput
import collections

def part1(puzzle_input, debug):
    tree = create_tree(puzzle_input, False)
    search_bag = "shiny gold"

    bags = 0
    for bag in tree.keys():
        if bag == search_bag:
            continue
        if does_bag_contain(tree, search_bag, bag):
            bags += 1

    return bags

def part2(input, debug):
    tree = create_tree(puzzle_input, False)
    search_bag = "shiny gold"

    # tree looks like this {
    # 'bright white': {'shiny gold': 1}, 
    # 'dark olive': {'dotted black': 4, 'faded blue': 3}
    # }

    bags = count_child_bags(tree, search_bag, 0) - 1

    # Off By 1 issue due to counting the shiny gold bag. Duh
    return bags -1

def create_tree(puzzle_input, debug):
    tree = {}

    for line in puzzle_input:
        # light red bags contain 1 bright white bag, 2 muted yellow bags.
        # Make processing easier
        line = line.replace("bags", "")
        line = line.replace("bag", "")
        line = line.replace(".", "")


        # split on word contain. 0 is the parent, 1 is children
        structure = line.split(' contain ')
        parent = structure[0].strip()
        children = structure[1].split(", ")

        # Seperate out the number from the colours as tuples, but check for the contains 'no other' strings
        # like this = [('1', 'bright white'), ('2', 'muted yellow')]
        tree_branch = [(child[0],child[2:]) for child in children if child[0] not in "no other"]

        # structure the tree with the parents name then the bits from the branch
        # like {'bright white': {'shiny gold': 1}, 'dark olive': {'dotted black': 4, 'faded blue': 3}}
        tree[parent] = {colour.strip(): int(number) for number, colour in tree_branch}

    return tree

def does_bag_contain(tree, search_colour, cur_colour):
    # WARNING: Recursion
    if search_colour == cur_colour:
        return True

    for bag in tree[cur_colour].keys():
        if does_bag_contain(tree, search_colour, bag):
            return True

    return False

def count_child_bags(tree, colour, i):
    # WARNING: Recursion
    total = 1
    for child, number in tree[colour].items():
        total += int(number) * count_child_bags(tree, child, i+1 )

    return total

with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input, False)
p2 = part2(puzzle_input, False)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )