import fileinput
import itertools

class initcode_computer:
    def __init__(self, puzzle_input_s):
        self.puzzle_input = [int(x) for x in puzzle_input_s]
        self.last_output = 0
        self.opt = 0
        self.i = 0

        # No more inputs for the option 3 list, if this is required but empty the class with end early and assume its going to be fed some more.
        self.opt3_no_more_inputs = False
        # print("initcode computer initialised")

    def execute(self, opt3_input):
            
        # print("execute is using", opt3_input)
        # return(a_mode, b_mode, c_mode, opt_code)


        # instructions = self.opt_code_split(int(self.puzzle_input[self.i]))
        # a_mode = instructions[0]
        # b_mode = instructions[1]
        # c_mode = instructions[2]
        # self.opt = instructions[3]


        # If opt3_no_more_inputs is true then the program has aborted early, and must have been given more inputs,
        if self.opt3_no_more_inputs == True and len(opt3_input) > 0:
            self.opt3_no_more_inputs = False
        else: 
            self.i = 0
        
        # Reset the incrementing pointer for this new execution
        
        

        while self.opt != 99 and self.opt3_no_more_inputs == False:
            # print(a_mode,b_mode,c_mode,opt,opt3_input)
            '''
            1,0,0,3,99
             \ \ \ \ c
              \ \ \ b
               \ \ a
                \ Opt
            '''

            instructions = self.opt_code_split(int(self.puzzle_input[self.i]))
            a_mode = instructions[0]
            b_mode = instructions[1]
            c_mode = instructions[2]
            self.opt = instructions[3]


            # param mode 0 is position mode (value at position)
            # param mode 1 is immediate mode (this position)
            if a_mode == 0 and self.opt != 99:
                a = self.puzzle_input[self.i+1]
            elif a_mode == 1:
                a = self.i+1

            # if self.opt 1
            # add self.i+1 and self.i+2 store answer in index self.i+3
            # skip to self.i+4
            if self.opt == 1:
                if b_mode == 0:
                    b = self.puzzle_input[self.i+2]
                elif b_mode == 1:
                    b = self.i+2

                if c_mode == 0:
                    c = self.puzzle_input[self.i+3]
                elif c_mode == 1:
                    c = self.i+3

                self.puzzle_input[c] = self.puzzle_input[a] + self.puzzle_input[b]
                self.i+=4

            # if self.opt 2
            # multiply self.i+1 and self.i+2 store answer in index self.i+3
            # skip to self.i+4
            if self.opt == 2:
                if b_mode == 0:
                    b = self.puzzle_input[self.i+2]
                elif b_mode == 1:
                    b = self.i+2

                if c_mode == 0:
                    c = self.puzzle_input[self.i+3]
                elif c_mode == 1:
                    c = self.i+3

                self.puzzle_input[c] = self.puzzle_input[a] * self.puzzle_input[b]
                self.i+=4

            # if self.opt 3
            # store input in position a
            # skip to self.i+2
            if self.opt == 3:
                if len(opt3_input) == 0:
                    # print("We have run out of inputs")
                    self.opt3_no_more_inputs = True
                    # break
                    
                else:
                    self.puzzle_input[a] = opt3_input.pop(0)
                    self.i += 2
            
            # if self.opt 4
            # output the value in position a
            # skip to self.i+2
            if self.opt == 4:
                # print(self.puzzle_input[a])
                # if self.last_output == 0:
                self.last_output = self.puzzle_input[a]
                    # print(self.last_output)
                # else:
                #    print("Something went wrong and the last output was not 0")
                
                self.i += 2


            # if self.opt 5
            # if first param IS NOT 0, set the instruction pointer to the value from the second paramater
            # skip to i= second param
            if self.opt == 5:
                if b_mode == 0:
                    b = self.puzzle_input[self.i+2]
                elif b_mode == 1:
                    b = self.i + 2

                if self.puzzle_input[a] != 0: 
                    self.i= self.puzzle_input[b]
                else:
                    self.i += 3

            # if self.opt 6
            # if first param IS 0, set the instruction pointer to the value from the second paramater
            # skip to i= second param
            if self.opt == 6:
                if b_mode == 0:
                    b = self.puzzle_input[self.i+2]
                elif b_mode == 1:
                    b = self.i + 2

                if self.puzzle_input[a] == 0: 
                    self.i= self.puzzle_input[b]
                else:
                    self.i+= 3


            # if self.opt 7
            # if first param is < second param, store '1' in the third param
            # skip to self.i+4
            if self.opt == 7:
                if b_mode == 0:
                    b = self.puzzle_input[self.i+2]
                elif b_mode == 1:
                    b = self.i+2

                if c_mode == 0:
                    c = self.puzzle_input[self.i+3]
                elif c_mode == 1:
                    c = self.i+3

                if self.puzzle_input[a] < self.puzzle_input[b]:
                    self.puzzle_input[c] = 1
                else:
                    self.puzzle_input[c] = 0
                
                self.i+= 4


            # if self.opt 8
            # if fierst param is == second param, store 1 in the third param
            # skip to self.i+4
            if self.opt == 8:
                if b_mode == 0:
                    b = self.puzzle_input[self.i+2]
                elif b_mode == 1:
                    b = self.i+2

                if c_mode == 0:
                    c = self.puzzle_input[self.i+3]
                elif c_mode == 1:
                    c = self.i+3

                if self.puzzle_input[a] == self.puzzle_input[b]:
                    self.puzzle_input[c] = 1
                else:
                    self.puzzle_input[c] = 0
                
                self.i+= 4

            
            # instructions = self.opt_code_split(int(self.puzzle_input[self.i]))
            # a_mode = instructions[0]
            # b_mode = instructions[1]
            # c_mode = instructions[2]
            # self.opt = instructions[3]
            


        # if 99 stop
        return self.last_output


    def opt_code_split(self, instruction):
        # Instruction could be anything from 0 to 10000
        # ABCDE
        #  1002

        # DE - two-digit opcode,      02 == opcode 2
        #  C - mode of 1st parameter,  0 == position mode
        #  B - mode of 2nd parameter,  1 == immediate mode
        #  A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
        # instruction_list = str(instruction).split()
        instruction_list = [j for j in str(instruction)]

        while len(instruction_list) < 5:
            instruction_list.insert(0,'0')

        opt_code = int(instruction_list[3] + instruction_list[4])

        # return(a_mode, b_mode, c_mode, opt_code)
        return(int(instruction_list[2]), int(instruction_list[1]), int(instruction_list[0]), opt_code)





def part1(puzzle_input):

    phase_orders = list(itertools.permutations([0,1,2,3,4]))
    
    # # sample code bits
    # # comment out for live
    # sample1 = (4,3,2,1,0)
    # sample2 = (0,1,2,3,4)
    # sample3 = (1,0,4,3,2)
    # phase_orders = [sample2]
    # # end sample


    # This should be the next order in the phase
    heighest_signal = 0
    heighest_signal_combination = []

    for current_order in phase_orders:

        amp_a = initcode_computer(puzzle_input)
        amp_b = initcode_computer(puzzle_input)
        amp_c = initcode_computer(puzzle_input)
        amp_d = initcode_computer(puzzle_input)
        amp_e = initcode_computer(puzzle_input)
        

        # print(current_order[0])
        # prepare amp a with the phase
        amp_a.execute([current_order[0], 0])

        # prepare amp b with the phase
        amp_b.execute([current_order[1],amp_a.last_output])


        # prepare amp c with the phase
        amp_c.execute([current_order[2],amp_b.last_output])


        # prepare amp d with the phase
        amp_d.execute([current_order[3],amp_c.last_output])


        # prepare amp b with the phase
        amp_e.execute([current_order[4],amp_d.last_output])       
         

        # print("completed:", current_order, " = ", amp_e.last_output)

        if amp_e.last_output > heighest_signal:
            # print(amp_e.last_output)
            heighest_signal = amp_e.last_output
            heighest_signal_combination = current_order
    

    return(heighest_signal, heighest_signal_combination)



def part2(puzzle_input):

    phase_orders = list(itertools.permutations([5,6,7,8,9]))
        
    # # sample code bits
    # # comment out for live
    # sample1 = (9,8,7,6,5)
    # sample2 = (9,7,8,5,6)
    # phase_orders = [sample1]
    # # end sample



    # This should be the next order in the phase
    heighest_signal = 0
    heighest_signal_combination = []

    for current_order in phase_orders:
        amp_a = initcode_computer(puzzle_input)
        amp_b = initcode_computer(puzzle_input)
        amp_c = initcode_computer(puzzle_input)
        amp_d = initcode_computer(puzzle_input)
        amp_e = initcode_computer(puzzle_input)

        # Run first execution with the extra phase input
        amp_a.execute([current_order[0], amp_e.last_output])

        # prepare amp b with the phase
        amp_b.execute([current_order[1],amp_a.last_output])

        # prepare amp c with the phase
        amp_c.execute([current_order[2],amp_b.last_output])

        # prepare amp d with the phase
        amp_d.execute([current_order[3],amp_c.last_output])

        # prepare amp b with the phase
        amp_e.execute([current_order[4],amp_d.last_output])    


        while amp_e.opt != 99:  

            # print(current_order[0])
            # prepare amp a with the phase
            amp_a.execute([amp_e.last_output])

            # prepare amp b with the phase
            amp_b.execute([amp_a.last_output])


            # prepare amp c with the phase
            amp_c.execute([amp_b.last_output])


            # prepare amp d with the phase
            amp_d.execute([amp_c.last_output])


            # prepare amp b with the phase
            amp_e.execute([amp_d.last_output])    
            

        print("completed:", current_order, " = ", amp_e.last_output)
        # sample1 should be 139629729
        # sample2 should be 18216

        if amp_e.last_output > heighest_signal:
            # print(amp_e.last_output)
            heighest_signal = amp_e.last_output
            heighest_signal_combination = current_order
    

    return(heighest_signal, heighest_signal_combination)





with open('input.txt', 'r') as myfile:
    puzzle_input_s = (myfile.read()).split(",")

print("part1:", part1(puzzle_input_s))

print("part2:", part2(puzzle_input_s))
