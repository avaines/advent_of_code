"""
Day X: Title
"""
import fileinput
import collections


def part1(puzzle_input, debug):
    preamble = 5
    weak_value = 0

    for l in range(preamble, len(puzzle_input)):
        checksum = puzzle_input[l - preamble : l]
        if debug: print("current pointer is ",puzzle_input[l],"- current checksum is", checksum)

        for check_a in checksum:
            check_a = int(check_a)

            for check_b in checksum:
                check_b = int(check_b)

                if check_a == check_b: continue # Not sure about this?

                if debug: print("Checking ",puzzle_input[l],"- current checksum is", check_a, "+", check_b, "(", check_a + check_b, ")")

                if check_a + check_b != puzzle_input[l]:
                    weak_value = puzzle_input[l]
                else:
                    if debug: print("Checksum found ",puzzle_input[l],"- current checksum is", check_a, "+", check_b, "(", check_a + check_b, ")")
                    # these two do add up, so this index is sane
                    weak_value = 0
                    break

            if weak_value != 0 and check_a == checksum[-1]:
                # Nothing in index's checksum worked
                if debug: print(puzzle_input[l], "is insecure")



    return weak_value


def part2(input, debug):
    return 0


with open('sample.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

p1 = part1(puzzle_input, True)
p2 = part2(puzzle_input, False)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )