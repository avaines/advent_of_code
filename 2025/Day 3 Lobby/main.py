# pylint: disable-all
# Import AOC Common
import os
import sys
import time

sys.path.append("../")
from shared import aoc_common, aoc_algorithms


P1_DEBUG = True
P2_DEBUG = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data()
INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def part1(input):
    battteryCombos=[]

    for batteryBank in input:
        batteryBankLst = [int(x) for x in str(batteryBank)]

        batteryOneValue = max(batteryBankLst)
        batteryOneIndex = batteryBankLst.index(batteryOneValue)

        if batteryOneIndex == len(batteryBankLst)-1:
            batteryBankLst.pop(batteryOneIndex)
            batteryTwoValue = max(batteryBankLst)
            battteryCombos.append(int(str(batteryTwoValue)+str(batteryOneValue)))
        else:
            batteryTwoValue = max(batteryBankLst[batteryOneIndex+1::])
            battteryCombos.append(int(str(batteryOneValue)+str(batteryTwoValue)))

    return sum(battteryCombos)


def part2(input):
    battteryCombos=[]

    for batteryBank in input:
        bankLength = len(batteryBank)
        bankJoltages= [ int(joltage) for joltage in batteryBank]
        batteriesLeft = 12
        batteriesEnabled = []
        bankIndex = -1

        for _ in range(batteriesLeft):
            # find max in bank after index
            searchSlice = bankJoltages[bankIndex+1: bankLength - batteriesLeft +1]
            batteryJoltage = max(searchSlice)

            # find pos of max in bank after index
            bankIndex = bankJoltages.index(batteryJoltage, bankIndex+1)

            # add it to the enabled batteries
            batteriesEnabled.append(batteryJoltage)
            batteriesLeft -= 1

        # add it to the combos
        battteryCombos.append(int("".join([str(x) for x in batteriesEnabled])))

    if P2_DEBUG: print(battteryCombos) # Sample: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
    return sum(battteryCombos)


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    start_time_part1 = time.time()
    part_1 = part1(parsed_input)
    end_time_part1 = time.time()

    start_time_part2 = time.time()
    part_2 = part2(parsed_input)
    end_time_part2 = time.time()

    print("# # # SOLUTIONS # # #")
    print(f"Part 1: {part_1} \t ⏱️ in {end_time_part1 - start_time_part1:.4f} seconds")
    print(f"Part 2: {part_2} \t ⏱️ in {end_time_part2 - start_time_part2:.4f} seconds")
