"""
task summary/notes
"""

import fileinput
import collections

def part1(forms, debug):
    sum_of_counts = 0

    for i in forms:
        group = forms[i]
        group_unique = list(set(group['data']))
        if debug: print(group, "=", len(group_unique))
        sum_of_counts = sum_of_counts + len(group_unique)

    return sum_of_counts


def part2(forms, debug):
    sum_of_counts = 0

    for i in forms:
        group = forms[i]
        group_unique = list(set(group['data']))

        for char in group_unique:
            occurences = group['data'].count(char)
            if occurences == group['entries']:
                if debug: print("There is", occurences, "occurence of", char, "in", group['data'])
                sum_of_counts +=1


    return sum_of_counts

def chunk_batch_file(puzzle_input):
    data = {}
    list_of_objects = []
    map_of_objects=[]

    for line in puzzle_input.split("\n\n"):
        # Split the file on the new lines
        list_of_objects.append(line)

    for i in range(0, len(list_of_objects)):
        data_object = {}
        data_object['entries'] = list_of_objects[i].count('\n')+1
        data_object['data'] = list_of_objects[i].replace("\n", "")
        data[i] = data_object

    # data = {
    #   0: {
    #       'data': 'abc',
    #       'entries': 1
    #    },
    #   1: {
    #       'data': 'abc', 
    #       'entries': 3
    #       }
    # }
    return data


with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read()

form_list = chunk_batch_file(puzzle_input)

p1 = part1(form_list, False)
p2 = part2(form_list, False)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )