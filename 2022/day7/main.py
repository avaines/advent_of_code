import os
from collections import defaultdict

INPUT_DEBUG = False
P1_DEBUG    = False
P2_DEBUG    = True

USE_REAL_DATA = True # Loads input.txt when True or sample.txt when False

INPUT_FILENAME  = "%s/input.txt" % os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILENAME = "%s/sample.txt" % os.path.dirname(os.path.realpath(__file__))


def input_parser(input):
    file_sizes = defaultdict(int) # TIL default dicts return a default value if you try access a key that doesnt exist. Without this adding the filesizes to a path that doesnt already exist errors.

    paths = []

    for command in input:
        command_args = command.split()
        if command_args[1] == "cd":
            if command_args[2] == "..":
                paths.pop()
            else:
                paths.append(command_args[2])

        elif command_args[1] == "ls":
            if INPUT_DEBUG: print("what files are in", paths[-1])
        elif command_args[0] == "dir": # Sneeky, the dir commands are not prefixed with $'s
            if INPUT_DEBUG: print("current path is", paths[-1])
        else:

            file_size = int(command_args[0])

            # Add the file's size to the dir size and the size of all parents
            for i in range(1, len(paths)+1):
                file_sizes[''.join(paths[:i])] += file_size

    return file_sizes

def part1(input):
    total_size = 0
    for path, size in input.items():
        if size <= 100000:
            if P1_DEBUG: print(path, "is under 100,000")
            total_size += size

    return total_size


def part2(input):
    total_disk_space = 70000000
    space_needed_for_update = 30000000
    used_disk_space = input['/']
    unused_disk_space = total_disk_space- used_disk_space

    need_to_free = used_disk_space - (total_disk_space - space_needed_for_update)
    directory_size_of_deletion_candidate = input['/']

    for path, size in input.items():
        if size >= need_to_free:
            directory_size_of_deletion_candidate = min(directory_size_of_deletion_candidate,size)
            if P1_DEBUG: print(path, "is under 100,000")

    return directory_size_of_deletion_candidate


if __name__ == '__main__':
    with open(INPUT_FILENAME if USE_REAL_DATA else SAMPLE_FILENAME, 'r') as input_file:
        parsed_input = input_parser(input_file.read().split("\n"))

    print()
    part_1 = part1(parsed_input)
    part_2 = part2(parsed_input)

    print("# # # SOLUTIONS # # #")
    print("Part1:", part_1 )
    print("Part2:", part_2 )
