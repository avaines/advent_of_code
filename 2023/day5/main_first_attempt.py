
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
from datetime import datetime
import collections

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False
if USE_REAL_DATA: aoc_common.get_aoc_puzzle_data(2023, 5)

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


    def process_ranges(self, map):
        completed_map = dict()

        for row in map:
            dest_rng_start, src_rng_start, rng_len = row.split()
            dst_range = [i for i in range(int(dest_rng_start), int(dest_rng_start) + int(rng_len))]
            src_range = [i for i in range(int(src_rng_start), int(src_rng_start) + int(rng_len))]
            completed_map.update(dict(zip(src_range, dst_range)))

        return completed_map


    def process_all_maps(self):
        s2s_map = self.process_ranges(self.seeds_to_soil)
        s2f_map = self.process_ranges(self.soil_to_fertilizer)
        f2w_map = self.process_ranges(self.fertilizer_to_water)
        w2l_map = self.process_ranges(self.water_to_light)
        l2t_map = self.process_ranges(self.light_to_temp)
        t2h_map = self.process_ranges(self.temp_to_hum)
        h2l_map = self.process_ranges(self.hum_to_location)

        for seed in self.seeds:
            tmp_store = {
                "soil": int(seed),
                "fertilizer": int(seed),
                "water": int(seed),
                "light": int(seed),
                "temp": int(seed),
                "humidity": int(seed),
                "location": int(seed)
            }

            tmp_store["soil"] = s2s_map[int(seed)] if int(seed) in s2s_map else int(seed)
            tmp_store["fertilizer"] = s2f_map[int(seed)] if int(seed) in s2f_map else tmp_store["soil"]
            tmp_store["water"] = f2w_map[tmp_store["fertilizer"]] if tmp_store["fertilizer"] in f2w_map else tmp_store["fertilizer"]
            tmp_store["light"] = w2l_map[tmp_store["water"]] if tmp_store["water"] in w2l_map else tmp_store["water"]
            tmp_store["temp"] = l2t_map[tmp_store["light"]] if tmp_store["light"] in l2t_map else tmp_store["light"]
            tmp_store["humidity"] = t2h_map[tmp_store["temp"]] if tmp_store["temp"] in t2h_map else tmp_store["temp"]
            tmp_store["location"] = h2l_map[tmp_store["humidity"]] if tmp_store["humidity"] in h2l_map else tmp_store["humidity"]

            self.seed_result_map[int(seed)] = tmp_store

        if P1_DEBUG:
            for s in list(map(int, self.seeds)):
                print(f'Seed {s} has soil {self.seed_result_map[s]["soil"]}, fertilizer {self.seed_result_map[s]["fertilizer"]}, water {self.seed_result_map[s]["water"]}, light {self.seed_result_map[s]["light"]}, temp {self.seed_result_map[s]["temp"]}, humidity {self.seed_result_map[s]["humidity"]}, location {self.seed_result_map[s]["location"]}')


    def get_lowest_location_numbers(self):
        lowest_min = None

        for seed in self.seeds:
            if lowest_min == None: lowest_min = self.seed_result_map[int(seed)]["location"]
            lowest_min = min(lowest_min, self.seed_result_map[int(seed)]["location"])

        return lowest_min


def part1():
    ALMANAC.process_all_maps()

    return ALMANAC.get_lowest_location_numbers()


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
