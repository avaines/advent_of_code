
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from datetime import datetime
import collections

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

class almanac:
    def __init__(self, map):
        self.seeds = map[0].split(": ")[1].split()

        self.seeds_to_soil = map[1].split(":\n")[1].splitlines()
        self.soil_to_fertilizer = map[2].split(":\n")[1].splitlines()
        self.fertilizer_to_water = map[3].split(":\n")[1].splitlines()
        self.water_to_light = map[4].split(":\n")[1].splitlines()
        self.light_to_temp = map[5].split(":\n")[1].splitlines()
        self.temp_to_hum = map[6].split(":\n")[1].splitlines()
        self.hum_to_location = map[7].split(":\n")[1].splitlines()

        self.seed_result_map = collections.defaultdict(dict)



def part1():
    def process_map(map, seed):
        for entry in map:
            if seed >= entry[1] and seed < (entry[1] + entry[2]):
                return seed - entry[1] + entry[0]
        return seed

    # ALMANAC.process_all_maps()
    merged_maps = [
        [list(map(int, i.split())) for i in ALMANAC.seeds_to_soil],
        [list(map(int, i.split())) for i in ALMANAC.soil_to_fertilizer],
        [list(map(int, i.split())) for i in ALMANAC.fertilizer_to_water],
        [list(map(int, i.split())) for i in ALMANAC.water_to_light],
        [list(map(int, i.split())) for i in ALMANAC.light_to_temp],
        [list(map(int, i.split())) for i in ALMANAC.temp_to_hum],
        [list(map(int, i.split())) for i in ALMANAC.hum_to_location],
    ]

    result = []
    for seed in ALMANAC.seeds:
        for m in merged_maps:
            seed = process_map(m, int(seed))
        result.append(seed)


    return min(result)


def part2(input):
    if P2_DEBUG: print("Doing Part 2 things")
    return "part 2 answer"


if __name__ == '__main__':
    startTime = datetime.now()
    parsed_input = aoc_common.import_file_double_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    ALMANAC = almanac(parsed_input)

    part_1 = part1()
    part_2 = part2(parsed_input)


    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
