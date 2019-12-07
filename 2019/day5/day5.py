"""
task summary/notes
""" 

import fileinput

def part1and2(opt3_input):
    # def part1(noun, verb, opt3_input):
    with open('input.txt', 'r') as myfile:
        puzzle_input_s = (myfile.read()).split(",")
    
    puzzle_input = [int(x) for x in puzzle_input_s]

    i = 0

    # return(a_mode, b_mode, c_mode, opt_code)
    instructions = opt_code_split(int(puzzle_input[i]))
    a_mode = instructions[0]
    b_mode = instructions[1]
    c_mode = instructions[2]
    opt = instructions[3]

    last_output = 0

    while opt != 99:
        '''
        1,0,0,3,99
         \ \ \ \ c
          \ \ \ b
           \ \ a
            \ Opt
        '''
        
         # param mode 0 is position mode (value at position)
         # param mode 1 is immediate mode (this position)
        if a_mode == 0:
            a = puzzle_input[i+1]
        elif a_mode == 1:
            a = i+1

        # if opt 1
        # add i+1 and i+2 store answer in index i+3
        # skip to i+4
        if opt == 1:
            if b_mode == 0:
                b = puzzle_input[i+2]
            elif b_mode == 1:
                b = i+2

            if c_mode == 0:
                c = puzzle_input[i+3]
            elif c_mode == 1:
                c = i+3

            puzzle_input[c] = puzzle_input[a] + puzzle_input[b]
            i +=4

        # if opt 2
        # multiply i+1 and i+2 store answer in index i+3
        # skip to i+4
        if opt == 2:
            if b_mode == 0:
                b = puzzle_input[i+2]
            elif b_mode == 1:
                b = i+2

            if c_mode == 0:
                c = puzzle_input[i+3]
            elif c_mode == 1:
                c = i+3

            puzzle_input[c] = puzzle_input[a] * puzzle_input[b]
            i +=4

        # if opt 3
        # store input in position a
        # skip to i+2
        if opt ==3:
            puzzle_input[a] = opt3_input
            i += 2
        
        # if opt 4
        # output the value in position a
        # skip to i+2
        if opt ==4:
            # print(puzzle_input[a])
            if last_output == 0:
                last_output = puzzle_input[a]
            else:
                return "Something went wrong and the last output was not 0"
            i += 2


        # if opt 5
        # if first param IS NOT 0, set the instruction pointer to the value from the second paramater
        # skip to i= second param
        if opt == 5:
            if b_mode == 0:
                b = puzzle_input[i+2]
            elif b_mode == 1:
                b = i+2

            if puzzle_input[a] != 0: 
                i = puzzle_input[b]
            else:
                i += 3

        # if opt 6
        # if first param IS 0, set the instruction pointer to the value from the second paramater
        # skip to i= second param
        if opt == 6:
            if b_mode == 0:
                b = puzzle_input[i+2]
            elif b_mode == 1:
                b = i+2

            if puzzle_input[a] == 0: 
                i = puzzle_input[b]
            else:
                i += 3


        # if opt 7
        # if first param is < second param, store '1' in the third param
        # skip to i+4
        if opt == 7:
            if b_mode == 0:
                b = puzzle_input[i+2]
            elif b_mode == 1:
                b = i+2

            if c_mode == 0:
                c = puzzle_input[i+3]
            elif c_mode == 1:
                c = i+3

            if puzzle_input[a] < puzzle_input[b]:
                puzzle_input[c] = 1
            else:
                puzzle_input[c] = 0
            
            i += 4


        # if opt 8
        # if fierst param is == second param, store 1 in the third param
        # skip to i+4
        if opt == 8:
            if b_mode == 0:
                b = puzzle_input[i+2]
            elif b_mode == 1:
                b = i+2

            if c_mode == 0:
                c = puzzle_input[i+3]
            elif c_mode == 1:
                c = i+3

            if puzzle_input[a] == puzzle_input[b]:
                puzzle_input[c] = 1
            else:
                puzzle_input[c] = 0
            
            i += 4



        
        instructions = opt_code_split(int(puzzle_input[i]))
        a_mode = instructions[0]
        b_mode = instructions[1]
        c_mode = instructions[2]
        opt = instructions[3]
        # opt = int(puzzle_input[i])
    
    # if 99 stop
    return last_output




def opt_code_split(instruction):
    # Instruction could be anything from 0 to 10000
    # ABCDE
    #  1002

    # DE - two-digit opcode,      02 == opcode 2
    #  C - mode of 1st parameter,  0 == position mode
    #  B - mode of 2nd parameter,  1 == immediate mode
    #  A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
    # instruction_list = str(instruction).split()
    instruction_list = [i for i in str(instruction)]

    while len(instruction_list) < 5:
        instruction_list.insert(0,'0')

    opt_code = int(instruction_list[3] + instruction_list[4])

    # return(a_mode, b_mode, c_mode, opt_code)
    return(int(instruction_list[2]), int(instruction_list[1]), int(instruction_list[0]), opt_code)



# print("part1:", part1(12,2,4))
print("part1:", part1and2(1))
print("part2:", part1and2(5))