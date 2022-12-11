import os
import operator
import math

INPUT_DEBUG = True
P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))

class MonkeyBrain():
    def __init__(self, monkey_config, debug=False):
        self.debug = debug

        self.id = 0
        self.div_three_on_inspection = False # Part 1 sets to True
        self.item_worry_levels = [] # Worry level for each item monkey is holding and order they will be inspected
        self.operation = "" # worry level changes on monkey inspection of items
        self.test_mod = 0
        self.test_true_target = 0
        self.test_false_target = 0
        self.parse_monkey_config(monkey_config)

        self.test_mod_lcm = self.test_mod # When using part2 mode (div_thrre_no_inspection == False) set this to the LCM of all possible monkey test_mod's
        self.inspection_count = 0

    def parse_monkey_config(self, config):
        #Monkey 0:
        config = config.split("\n")
        self.monkey_id = config[0].split()[1]

        #   Starting items: 79, 98
        monkey_item_worry_levels_raw = config[1].split(":")[1].strip()
        self.item_worry_levels = monkey_item_worry_levels_raw.split(", ")

        #   Operation: new = old * 19
        self.operation = config[2].split(":")[1].strip()

        # Test: divisible by 23
        monkey_test_raw = config[3].split(":")[1].strip()
        self.test_mod = int(monkey_test_raw.split()[-1])

        # If true: throw to monkey 2
        monkey_true_target_raw = config[4].split(":")[1].strip()
        self.test_true_target = int(monkey_true_target_raw.split()[-1])

        # If false: throw to monkey 3
        monkey_false_target_raw = config[5].split(":")[1].strip()
        self.test_false_target = int(monkey_false_target_raw.split()[-1])

    def calculate_item_target(self, item_worry_level):

        if int(item_worry_level) % self.test_mod == 0:
            if self.debug and self.div_three_on_inspection: print("\tCurrent worry level is divisible by", self.test_mod)
            return self.test_true_target
        else:
            if self.debug and self.div_three_on_inspection: print("\tCurrent worry level is NOT divisible by", self.test_mod)
            return self.test_false_target

    def catch_item(self, item_worry_level):
        self.item_worry_levels.append(item_worry_level)

    def inspect(self):
        actions = []
        while len(self.item_worry_levels) > 0:
            self.inspection_count += 1
            item_worry_level = self.item_worry_levels.pop(0)

            if self.debug and self.div_three_on_inspection: print("Monkey %s inspects an item with a worry level of %s" % (self.id, item_worry_level))
            item_worry_level = self.recalculate_item_worry_level_operation(item_worry_level)

            if self.div_three_on_inspection:
                item_worry_level = int(item_worry_level) // 3
                if self.debug and self.div_three_on_inspection: print("\tMonkey gets bored with item. Worry level is divided by 3 to", item_worry_level)
            else:
                # the part 2 case needs the LCM of the test_mods from all monkeys
                item_worry_level = int(item_worry_level) % self.test_mod_lcm

            throw_target = self.calculate_item_target(item_worry_level)
            if self.debug and self.div_three_on_inspection: print("\tItem with worry level", item_worry_level, "is thrown to monkey", throw_target)

            actions.append([item_worry_level, throw_target])

        return actions

    def recalculate_item_worry_level_operation(self, item_worry_level):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        operation = self.operation.split()

        if operation[2] == "old": operation[2] = item_worry_level
        if operation[4] == "old": operation[4] = item_worry_level

        if self.debug and self.div_three_on_inspection: print("\tWorry level is", operation[3], "by", operation[4], "to ", end="")
        item_worry_level = ops[operation[3]](int(operation[2]), int(operation[4]))
        if self.debug and self.div_three_on_inspection: print(item_worry_level)

        return item_worry_level


def input_parser(input):
    return input

def part1(input):
    monkeys = dict()

    for config in range(len(input)):
        monkeys[config] = MonkeyBrain(monkey_config=input[config], debug=P1_DEBUG)

    if P1_DEBUG: {setattr(monkeys[m], "debug", P1_DEBUG) for m in monkeys}
    {setattr(monkeys[m], "div_three_on_inspection", True) for m in monkeys}

    for _ in range(20):
        for monkey_index in monkeys:
            monkey = monkeys[monkey_index]

            for monkey_action in monkey.inspect():
                monkeys[monkey_action[1]].catch_item(monkey_action[0])

        if P1_DEBUG: print()

    inspection_counts = sorted([monkeys[m].inspection_count for m in monkeys ])
    monkey_business = inspection_counts[-2] * inspection_counts[-1]

    return monkey_business

def part2(input):
    monkeys = dict()

    for config in range(len(input)):
        monkeys[config] = MonkeyBrain(monkey_config=input[config], debug=P1_DEBUG)

    if P2_DEBUG: {setattr(monkeys[m], "debug", P2_DEBUG) for m in monkeys}

    # large worried number workaround
    monkey_test_mod_lcm = math.lcm(*[monkey.test_mod for monkey in monkeys.values()])

    for cur_round in range(10000):
        if P2_DEBUG and cur_round % 100 == 0: print("Processing round:", cur_round)

        for monkey_index in monkeys:
            monkey = monkeys[monkey_index]
            setattr(monkey, "test_mod_lcm", monkey_test_mod_lcm) # Set the monkey test_mod_lcm value directly as a product of all other monkey test values

            for monkey_action in monkey.inspect():
                monkeys[monkey_action[1]].catch_item(monkey_action[0])

    inspection_counts = sorted([monkeys[m].inspection_count for m in monkeys ])
    monkey_business = inspection_counts[-2] * inspection_counts[-1]

    return monkey_business


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n\n"))

    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )