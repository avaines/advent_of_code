"""
task summary/notes
""" 

import fileinput

puzzle_input = list(fileinput.input('input.txt'))


def part1():
    # sample1 should be 34241
    fuel_total=0

    for line in puzzle_input:
        fuel = (int(line)/3)-2
        # print(int(line), "needs", int(fuel))

        fuel_total += int(fuel)
    
    return("P1 Total= ", int(fuel_total))
   

def part2():

    fuel_total=0

    for line in puzzle_input:
        fuel = get_fuel(int(line))
        extra_fuel = fuel
        print(int(line), "needs", int(fuel))

        while fuel >= 2:
            # print(int(line), ":- ", int(fuel), "needs an extra", int(get_fuel(int(fuel))), int(extra_fuel))
            fuel = get_fuel(int(fuel))

            extra_fuel += int(fuel)

        fuel_total += int(extra_fuel)
    
    return("P2 Total= ", int(fuel_total))


def get_fuel(weight):
    fuel = (weight/3)-2
    if int(fuel) < 0:
        fuel = 0
    # print("get_fuel:",fuel)
    return(fuel)


print(part1())
print(part2())