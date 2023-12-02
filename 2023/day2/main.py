
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def split_game_strings(game_details):
    game_id, game_rounds = game_details.split(": ")
    game_rounds = game_rounds.split("; ")

    return game_id, [gr.split(", ") for gr in game_rounds]

def part1(input):
    max_red_cubes=12
    max_green_cubes=13
    max_blue_cubes=14
    valid_games=[]
    invalid_games=[]

    for game in input:
        game_id, game_round_data = split_game_strings(game)

        totals = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }

        for game_round in game_round_data:

            for cube_draw in game_round:
                num_cubes, colour = cube_draw.split(" ")
                totals[colour] = max(totals[colour], int(num_cubes))

        if totals["red"] > max_red_cubes or totals["green"] > max_green_cubes or totals["blue"] > max_blue_cubes:
            if P1_DEBUG: print(f"{game} uses too many cubes")
            invalid_games.append(game_id.split(" ")[1])
        else:
            valid_games.append(game_id.split(" ")[1])

    return sum(list(map(int, valid_games)))

def part2(input):
    game_power=[]

    for game in input:
        game_id, game_round_data = split_game_strings(game)

        totals = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }

        round_game_power=[]
        for game_round in game_round_data:
            for cube_draw in game_round:
                num_cubes, colour = cube_draw.split(" ")
                totals[colour] = max(totals[colour], int(num_cubes))

            round_game_power.append(int(totals["red"]) * int(totals["green"]) * int(totals["blue"]))

        game_power.append(max(round_game_power))

    return sum(list(map(int, game_power)))


if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
