"""
task summary/notes
""" 

import fileinput


def part1(noun, verb):
    # puzzle_input = fileinput.input('sample1.txt')
    with open('input.txt', 'r') as myfile:
        puzzle_input_s = (myfile.read()).split(",")
    
    puzzle_input = [int(x) for x in puzzle_input_s]


    puzzle_input[1] = noun
    puzzle_input[2] = verb

    opt = 0
    i = 0

    keep_running = True

    while opt != 99:
        # target = puzzle_input[puzzle_input[i+3]]
        # if 1
        # add i+1 and i+2 store answer in index i+3
        # skip to i+4
        a = puzzle_input[i+1]
        b = puzzle_input[i+2]
        c = puzzle_input[i+3]

        if opt == 1:
            puzzle_input[c] = puzzle_input[a] + puzzle_input[b]
           
        # if 2
        # multiply i+1 and i+2 store answer in index i+3
        # skip to i+4
        if opt == 2:
            puzzle_input[c] = puzzle_input[a] * puzzle_input[b]

        i +=4

        opt = int(puzzle_input[i])
    
    # if 99 stop
    return puzzle_input[0]




def part2():

    for noun in range(0,100):
        for verb in range(0,100):
            r = part1(noun,verb)
            if r == 19690720:
                print(noun,verb)
                return 100 * noun + verb
    return noun, verb


# for i in range(0, len(puzzle_input)): 
#     puzzle_input[i] = int(puzzle_input[i]) 
# This is a better way f doing the two above lines: (AN)


print("part1:", part1(12,2))

print("part2:", part2())