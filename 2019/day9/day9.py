
from intcode import intcode_computer

def part1(BOOST):

    boost_ic = intcode_computer(BOOST)
    boost_ic.execute([1])

    return boost_ic.last_output


def part2(BOOST):
    boost_ic = intcode_computer(BOOST)
    boost_ic.execute([2])

    return boost_ic.last_output




with open('input.txt', 'r') as myfile:
    puzzle_input_s = (myfile.read()).split(",")

print("part1:", part1(puzzle_input_s))

print("part2:", part2(puzzle_input_s))
