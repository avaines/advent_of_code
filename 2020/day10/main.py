"""
Day X: Title
"""
import itertools
from os import curdir

def part1(puzzle_input, debug):
    max_joltage = max(puzzle_input) + 3
    puzzle_input.append(max_joltage)
    diff_1_jolts = 0
    diff_2_jolts = 0
    diff_3_jolts = 0

    cur_adapter_joltage = 0

    while cur_adapter_joltage != max(puzzle_input):
        next_adapter_joltage = min([j for j in puzzle_input if j > cur_adapter_joltage])
        if debug: print("current joltage:", cur_adapter_joltage, "next adapter has a joltage of:", next_adapter_joltage)

        if next_adapter_joltage - cur_adapter_joltage == 1: diff_1_jolts +=1
        elif next_adapter_joltage - cur_adapter_joltage == 2: diff_2_jolts +=1
        elif next_adapter_joltage - cur_adapter_joltage == 3: diff_3_jolts +=1

        cur_adapter_joltage = next_adapter_joltage

    return diff_1_jolts * diff_3_jolts


def part2(puzzle_input, debug):
    # Re-purposed the Dynamic programming approach from https://leetcode.com/problems/climbing-stairs/solution/
    # print(f'Answer: {ans[puzzle_input[-1]]}')
    puzzle_input.sort()
    puzzle_input.append( max( puzzle_input ) + 3 )

    dp = {}
    dp[0] = 1
    for adapter in puzzle_input:
        # The get() method returns the value of the item with the specified key. get(REQ:Keyname, OPT:Value to return if the key doesnt exist)
        dp[adapter] = dp.get(adapter -1, 0) + dp.get(adapter - 2, 0) + dp.get(adapter - 3, 0)
        if debug: print("found another combination, were up to:", dp[adapter])

    return dp[puzzle_input[-1]]


with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")

puzzle_input_ints = [ int(x) for x in puzzle_input ]

p1 = part1(puzzle_input_ints, False)
p2 = part2(puzzle_input_ints, True)

print("#############################################################")
print("Part1:", p1 )
print("Part2:", p2 )