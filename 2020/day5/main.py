"""
task summary/notes
"""

import fileinput
import collections

def get_partition(upper, lower, row, i):
    # WARNING: Recursion
    if upper == lower:
        # We've found the correct value, theres no upper or lower boundary closer than the current finger
        return upper

    if row[i] in "BR":
        # If its 'Back' or 'Right', its one is in the upper/back half. so reset the 'lower' counter to the higest value we've got left in that half
        # Next runns will narrow this down as needed
        lower = (upper - lower) // 2 + lower +1  # //  is a integer divsion (with out the remainder), / would be a floating-point one apparently

    elif row[i] in "FL":
        # If its 'Front' or 'Left', its one is in the lower/front half. so reset the 'upper' counter to the higest value we've got left in that half
        # Next runns will narrow this down as needed
        upper = (upper - lower) // 2 + lower

    else:
        # something went wrong
        return 0

    # Increment index and re-run the function to narrow in those boundaries
    i +=1
    return get_partition(upper, lower, row, i)


def part1(puzzle_input):
    seat_ids = []
    for boarding_pass in puzzle_input:
        row = boarding_pass[:7]
        row_num = get_partition(127, 0, row, 0)
        column = boarding_pass[-3:]
        column_num = get_partition(7, 0, column, 0)
        seat_ids.append(row_num * 8 + column_num)

    return max(seat_ids), seat_ids


def part2(used_seats, debug):
    used_seats.sort()
    used_seats_no_f_or_b = used_seats[1:-1]

    missing_seat = 0
    for x in range(used_seats_no_f_or_b[0], used_seats_no_f_or_b[-1]+1):
        if x not in used_seats_no_f_or_b:
            if missing_seat == 0:
                missing_seat = x
            else:
                # Something has gone wrong or we've got multiple empty seats
                return 0

    return missing_seat



with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input)
p2 = part2(p1[1], True)

print("#############################################################")
print("Part1: ", p1[0] )
print("Part2: ", p2 )