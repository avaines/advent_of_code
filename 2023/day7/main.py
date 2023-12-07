
# Import AOC Common
import os, sys
sys.path.append("../")
from shared import aoc_common, aoc_algorithms

P1_DEBUG    = True
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

def hand_to_numbers(cards, j_wild=False):
    cards_to_numbers_map = {
        "T": 10,
        "J": 1 if j_wild else 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    # dict.get() takes an option param to return a value if the value doesnt exist in the lookup key!
    # (return the actual value of the card if its not a picture)
    return [int(cards_to_numbers_map.get(i,i)) for i in cards]


def calculate_score(cards, j_wild=False):
    card_counter = {}
    types = {
        50: "five of a kind", #5x
        40: "four of a kind", #4x
        32: "full house", # 3x and 2x
        30: "three of a kind", #3x
        22: "two pair", #2x and 2x
        20: "one pair", #2x
        10: 'high card' #1x
    }

    jokers_in_hand = 0
    if j_wild:
        jokers_in_hand = cards.count("J")
        cards = [i for i in cards if i !="J"]

    for card in cards:
        card_counter[card] = cards.count(card)

    if 5 in card_counter.values() or jokers_in_hand == 5:
        rank_score = 50 # five of a kind
    elif 4 in card_counter.values():
        rank_score = 10 * (4 + jokers_in_hand) # four of a kind
    elif 3 in card_counter.values() and 2 in card_counter.values():
        rank_score = 32 # full house
    elif 3 in card_counter.values():
        rank_score = 10 * (3 + jokers_in_hand) # three of a kind
    elif 2 in card_counter.values() and list(card_counter.values()).count(2) == 2:
        rank_score = 22 + 10 * jokers_in_hand # two pair
    elif 2 in card_counter.values():
        rank_score = 10 * (2 + jokers_in_hand) # one pair
    else:
        rank_score = 10 * ( 1 + jokers_in_hand) # high card

    return rank_score, types[rank_score]


def process_hands(hands, wildcards=False):
    scored_hands = []
    for hand in hands:
        numbers = hand_to_numbers([*hand[0]], wildcards)
        score = calculate_score([*hand[0]], wildcards)
        hand_info = (numbers, int(hand[1]), score)
        scored_hands.append(hand_info)

    scored_hands = sorted(scored_hands, key=lambda hand: (hand[2], hand[0]))

    total_score = 0
    for index, hand in enumerate(scored_hands, 1):
        rank_score = index * hand[1]
        total_score += rank_score
        if P1_DEBUG or P2_DEBUG: print(f"{''.join(str(hand[0]))} is {hand[2][1]} ranked {rank_score}")

    return total_score

if __name__ == '__main__':
    parsed_input = aoc_common.import_file_single_new_line(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME)
    parsed_input = [i.split() for i in parsed_input]

    part_1 = process_hands(parsed_input, False)
    part_2 = process_hands(parsed_input, True)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
