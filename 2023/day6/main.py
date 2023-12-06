
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms
import regex as re

P1_DEBUG    = True
P2_DEBUG    = False

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def part1(input):
    time = [int(i) for i in re.findall(r'\b\d+\b', input[0].split(": ")[1])]
    distance = [int(i) for i in re.findall(r'\b\d+\b', input[1].split(": ")[1])]

    races = list(zip(time, distance))

    total_ways_to_beat_high_scores = []
    for race in races:
        if P1_DEBUG: print(f"Next Race: {race[0]}ms with a record of {race[1]}mm")
        total_ways_to_beat_high_scores_this_race = 0

        for ms_held in range(1,race[0]+1):
            # each second held the boat speed increases 1mm/ms
            # (raceTime - secondsHeld)*secondsHeld = distanceTraveled
            distance = (race[0] - ms_held)*ms_held
            if distance > race[1]:
                if P1_DEBUG: print(f"\tHolding the button for {ms_held}ms, results in a distance of {distance}mm, the previous record was {race[1]}mm")
                total_ways_to_beat_high_scores_this_race+=1

        if total_ways_to_beat_high_scores_this_race > 0: total_ways_to_beat_high_scores.append(total_ways_to_beat_high_scores_this_race)

    return aoc_common.product(total_ways_to_beat_high_scores)

def part2(input):
    time = "".join(re.findall(r'\b\d+\b', input[0].split(": ")[1]))
    distance = "".join(re.findall(r'\b\d+\b', input[1].split(": ")[1]))

    race = (int(time), int(distance))

    total_ways_to_beat_high_scores_this_race = 0

    for ms_held in range(1,race[0]+1):
        # each second held the boat speed increases 1mm/ms
        # (raceTime - secondsHeld)*secondsHeld = distanceTraveled
        distance = (race[0] - ms_held)*ms_held
        if distance > race[1]:
            if P2_DEBUG: print(f"\tHolding the button for {ms_held}ms, results in a distance of {distance}mm, the previous record was {race[1]}mm")
            total_ways_to_beat_high_scores_this_race+=1

    return total_ways_to_beat_high_scores_this_race


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )

