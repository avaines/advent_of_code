import os
from operator import methodcaller

INPUT_DEBUG = True
P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

class The_Game():
    def __init__(self):
        self.total_score = 0
        self.rock_points = 1
        self.paper_points = 2
        self.scissors_points = 3
        self.lost_match_points = 0
        self.draw_match_points = 3
        self.win_match_points = 6

    def play_round(self, DEBUG, elf_move, my_move):
        if DEBUG: print("playing round for", elf_move, "vs", my_move)

        if elf_move == "A" and my_move == "X":
            # Rock Rock
            self.total_score += self.rock_points + self.draw_match_points

        elif elf_move == "A" and my_move == "Y":
            # Rock Paper
            self.total_score += self.paper_points + self.win_match_points

        elif elf_move == "A" and my_move == "Z":
            # Rock Scisors
            self.total_score += self.scissors_points + self.lost_match_points


        if elf_move == "B" and my_move == "X":
            # Paper Rock
            self.total_score += self.rock_points + self.lost_match_points

        elif elf_move == "B" and my_move == "Y":
            # Paper Paper
            self.total_score += self.paper_points + self.draw_match_points

        elif elf_move == "B" and my_move == "Z":
            # Paper Scisors
            self.total_score += self.scissors_points + self.win_match_points


        if elf_move == "C" and my_move == "X":
            # Scisors Rock
            self.total_score += self.rock_points + self.win_match_points

        elif elf_move == "C" and my_move == "Y":
            # Scisors Paper
            self.total_score += self.paper_points + self.lost_match_points

        elif elf_move == "C" and my_move == "Z":
            # Scissors Scissors
            self.total_score += self.scissors_points + self.draw_match_points

    def calculate_round(self, DEBUG, elf_move, target_condition):
        # My play is still XYZ when feeding in to play_round
        # X = Rock
        # Y = Paper
        # Z = Scisors

        if target_condition == "X":
            # I need to LOOSE
            if elf_move == "A":
                self.play_round(DEBUG, elf_move, "Z")
            elif elf_move == "B":
                self.play_round(DEBUG, elf_move, "X")
            elif elf_move == "C":
                self.play_round(DEBUG, elf_move, "Y")

        if target_condition == "Y":
            # I need to DRAW
            if elf_move == "A":
                self.play_round(DEBUG, elf_move, "X")
            elif elf_move == "B":
                self.play_round(DEBUG, elf_move, "Y")
            elif elf_move == "C":
                self.play_round(DEBUG, elf_move, "Z")

        if target_condition == "Z":
            # I need to WIN
            if elf_move == "A":
                self.play_round(DEBUG, elf_move, "Y")
            elif elf_move == "B":
                self.play_round(DEBUG, elf_move, "Z")
            elif elf_move == "C":
                self.play_round(DEBUG, elf_move, "X")

    def get_score(self):
        return self.total_score


def input_parser(input):
    if INPUT_DEBUG: print("Parsing the input")

    return input

def part1(input):

    part1_game = The_Game()

    for elf_move, my_move in list(map(methodcaller("split", " "), input)):
        part1_game.play_round(P1_DEBUG, elf_move, my_move)

    return part1_game.total_score

def part2(input):
    part2_game = The_Game()

    for elf_move, target_condition in list(map(methodcaller("split", " "), input)):
        part2_game.calculate_round(P1_DEBUG, elf_move, target_condition)

    return part2_game.total_score


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    part_1 = part1(parsed_input)

    part_2 = part2(parsed_input)

    print()
    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
