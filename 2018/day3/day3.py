"""
Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.or example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
""" 


import fileinput
puzzle_input = list(fileinput.input('day3.txt'))
# day3.short.txt should = 533
# day3.sample.txt should = 4
# day3.tony.txt should = 119572



def part1():
    rectangles = []

    # for each rectangle
    for rectangle in puzzle_input:
        # convert the entry from the puzzle input in to the object with calculated area and coordinates
        rectangles.append(part1_split(rectangle))

    # 'rectangles' looks like this
    # [
    #  {'area': 609, 'coords': [...], 'raw': '#2 @ 63,65: 29x21', 'ref': '2', 'x_max': 92, 'x_min': 63, 'y_max': 86, 'y_min': 65}, 
    #  {'area': 650, 'coords': [...], 'raw': '#4 @ 58,62: 26x25', 'ref': '4', 'x_max': 84, 'x_min': 58, 'y_max': 87, 'y_min': 62}, 
    #  {'area': 220, 'coords': [...], 'raw': '#8 @ 56,58: 11x20', 'ref': '8', 'x_max': 67, 'x_min': 56, 'y_max': 78, 'y_min': 58}, 
    #  {'area': 400, 'coords': [...], 'raw': '#9 @ 24,24: 20x20', 'ref': '9', 'x_max': 44, 'x_min': 24, 'y_max': 44, 'y_min': 24}
    # ]

    duplicate_coords = list()
    # start a loop for each line/entry in the rectangles dictionary
    for i in range(0,len(rectangles)):
        source_rectangle=rectangles[i]
        # compare it to each line in the input
        for j in range(i+1, len(rectangles)):
            target_rectangle=rectangles[j]

            duplicate_coords.extend( list(set(source_rectangle['coords']).intersection(target_rectangle['coords'])) ) 

    return len(set(duplicate_coords))



def part1_split(line):
    # accept something like: #1 @ 1,3: 4x4

    # Split the line in to compnants on empty spaces
    seperated_line = line.split()

    # create an empty dictionary
    sections = dict();

    # drop the raw input in to a 'raw' entry ust in case
    sections['raw'] = line.strip()

    # get rid of the '#' in front of the reference and stick it in ref
    sections['ref'] = seperated_line[0].replace('#', '')

    # seperate the coordinates section in to a left and top edge distance
    coords = seperated_line[2].replace(':','').split(',')
    size = seperated_line[3].split('x')

    sections['x_min'] = int(coords[0])
    sections['x_max'] = sections['x_min'] + (int(size[0])  )

    sections['y_min'] = int(coords[1])
    sections['y_max'] = sections['y_min'] + (int(size[1]) )

    sections['area'] = (sections['x_max'] - sections['x_min'] ) * (sections['y_max'] - sections['y_min'] )

    # Get a list of all the coordinates the shape occupies
    sections['coords'] = list()
    for x in range(sections['x_min'],sections['x_max']):
        for y in range(sections['y_min'],sections['y_max']):
            
            grid_ref = ''.join([str(x),":", str(y)])
            sections['coords'].append(grid_ref)

    # print ( sections )
    return sections


def part2():
    rectangles = []

    # for each rectangle
    for rectangle in puzzle_input:
        # convert the entry from the puzzle input in to the object with calculated area and coordinates
        rectangles.append(part1_split(rectangle))

    # 'rectangles' looks like this
    # [
    #  {'area': 609, 'coords': [...], 'raw': '#2 @ 63,65: 29x21', 'ref': '2', 'x_max': 92, 'x_min': 63, 'y_max': 86, 'y_min': 65}, 
    #  {'area': 650, 'coords': [...], 'raw': '#4 @ 58,62: 26x25', 'ref': '4', 'x_max': 84, 'x_min': 58, 'y_max': 87, 'y_min': 62}, 
    #  {'area': 220, 'coords': [...], 'raw': '#8 @ 56,58: 11x20', 'ref': '8', 'x_max': 67, 'x_min': 56, 'y_max': 78, 'y_min': 58}, 
    #  {'area': 400, 'coords': [...], 'raw': '#9 @ 24,24: 20x20', 'ref': '9', 'x_max': 44, 'x_min': 24, 'y_max': 44, 'y_min': 24}
    # ]


    # start a loop for each line/entry in the rectangles dictionary
    for source_rectangle in rectangles:

        # start a counter for the number of times a rectangle has no intersection/overlap
        match_counter = 1

        # check the source rectangle against each target rectangle 
        for target_rectangle in rectangles:
            
            # if no intertsection/overlap is found increase the counter
            if len(list(set(source_rectangle['coords']).intersection(target_rectangle['coords']))) == 0:
                match_counter += 1

        # if this source rectangle has a count value the same length of the number of rectangles, we have found the match
        if match_counter == len(rectangles):
            return( source_rectangle['ref'] )
    return 0




print("Overlap", part1())
print(part2())