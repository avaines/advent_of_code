"""
task summary/notes
""" 

import fileinput
from collections import Counter

puzzle_input = list(fileinput.input('input.txt'))
wire_a = puzzle_input[0].split(",")
wire_b = puzzle_input[1].split(",")

# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7


def part1(wire_a, wire_b):
    wire_a_coords = []
    wire_b_coords = []

    wire_a_last_coord = (0,0)
    wire_b_last_coord = (0,0)

    for move in wire_a:
        # Use .last_coord as a starting point to update itself using the helper function
        wire_a_last_coords = make_move(wire_a_last_coord, move[0], int(move[1:len(move)]),"" )
        wire_a_last_coord = wire_a_last_coords[1]

        # add this value to the list
        wire_a_coords.extend(wire_a_last_coords[0])
    

    for move in wire_b:
        # Use .last_coord as a starting point to update itself using the helper function
        wire_b_last_coords = make_move(wire_b_last_coord, move[0], int(move[1:len(move)]),"" )
        wire_b_last_coord = wire_b_last_coords[1]

        # add this value to the list
        wire_b_coords.extend(wire_b_last_coords[0])
    

    matches = set(wire_a_coords).intersection(wire_b_coords)
    # matches = list((Counter(wire_a_coords) - Counter(wire_b_coords)).elements()) 
    # print(matches)


    lowest = 999999
    matching_coord = ()
    for match in matches:
        md = manhattan_distance((0,0), match) 
        if md < lowest and md > 0:
            lowest = md
            matching_coord = match

    return lowest, matches


def make_move(current,direction,steps,target):
    # print(current,direction,int(steps))
    new_coords = []
    last_coord = ()

    if direction == 'R':
        # steps = (current[0] + steps) - current[0]
        # for step in range((current[0] + steps) - current[0]):
        for step in range(steps):
            new_coords.append( (current[0] + step, current[1]) )

            # found the step2 bit, exit early
            if target == (current[0] + step, current[1]):
                last_coord = (current[0] + steps, current[1])
                return new_coords, last_coord, True
        
        last_coord = (current[0] + steps, current[1])


    # if direction == 'L':
    #     new_coord = (current[0] - steps, current[1])
    if direction == 'L':
        # steps = (current[0] - steps) - current[0]
        for step in range(steps):

            new_coords.append( (current[0] - step, current[1]) )

            # found the step2 bit, exit early
            if target == (current[0] - step, current[1]):
                last_coord = (current[0] + steps, current[1])
                return new_coords, last_coord, True
        
        last_coord = (current[0] - steps, current[1])


    # if direction == 'U':
    #     new_coord = (current[0],current[1] + steps)
    if direction == 'U':
        # steps = (current[1] + steps) - current[1]
        # for step in range(current[1] + (current[1] + steps)):
        for step in range(steps):
            new_coords.append( (current[0], current[1] + step) )

            # found the step2 bit, exit early
            if target == (current[0], current[1] + step):
                last_coord = (current[0], current[1] + step)
                return new_coords, last_coord, True
        
        last_coord = (current[0],current[1] + steps)


    # if direction == 'D':
    #     new_coord = (current[0],current[1] - steps)
    if direction == 'D':
        # steps = (current[1] - steps) - current[1]
        # for step in range(current[1] + (current[1] - steps)):
        for step in range(steps):
            new_coords.append( (current[0], current[1] - step) )

            # found the step2 bit, exit early
            if target == (current[0], current[1] - step):
                last_coord = (current[0], current[1] - step)
                return new_coords, last_coord, True
        
        last_coord = (current[0],current[1] - steps)

    return new_coords, last_coord, False


def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))


def part2(wire_a, wire_b, target):
    wire_a_coords = []
    wire_b_coords = []

    wire_a_last_coord = (0,0)
    wire_b_last_coord = (0,0)

    for move in wire_a:
        # Use .last_coord as a starting point to update itself using the helper function
        wire_a_last_coords = make_move(wire_a_last_coord, move[0], int(move[1:len(move)]), target)
        wire_a_last_coord = wire_a_last_coords[1]

        # add this value to the list
        wire_a_coords.extend(wire_a_last_coords[0])
        if wire_a_last_coords[2]:
            wire_a_length = len(wire_a_coords) -1
            # print("a", target, len(wire_a_coords))
            break

    for move in wire_b:
        # Use .last_coord as a starting point to update itself using the helper function
        wire_b_last_coords = make_move(wire_b_last_coord, move[0], int(move[1:len(move)]), target)
        wire_b_last_coord = wire_b_last_coords[1]

        # add this value to the list
        wire_b_coords.extend(wire_b_last_coords[0])
        if wire_b_last_coords[2]:
            wire_b_length = len(wire_b_coords) -1
            # print("b", target, len(wire_b_coords))
            break

    if wire_a_length >0 and wire_b_length >0:
        print(target, "; ", wire_a_length, "+", wire_b_length, "=", wire_a_length + wire_b_length)
        return (wire_a_length + wire_b_length)
    
    return 0


part1_ans=part1(wire_a, wire_b)
print("part1:" ,part1_ans[0])

p2_lowest = 999999
for target in part1_ans[1]:
    # print( part2(wire_a, wire_b, target ) )

    part2_ans=part2(wire_a, wire_b, target )
    if part2_ans < p2_lowest and part2_ans != 0:
        p2_lowest = part2_ans

print("part2:", p2_lowest)