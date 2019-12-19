
import fileinput
import itertools

class intcode_computer:
    def __init__(self, puzzle_input_s):
        self.puzzle_input = [int(x) for x in puzzle_input_s]
        self.last_output = []
        self.op_code = 0

        # ProgramCounter
        self.pc = 0

        self.relative_base = 0

        # Day 9 needs memory to be extended
        memory_expansion = [0]*10000
        self.puzzle_input.extend(memory_expansion)
            

        # No more inputs for the option 3 list, if this is required but empty the class with end early and assume its going to be fed some more.
        self.op_code3_no_more_inputs = False
        # print("initcode computer initialised")

    def execute(self, opt3_input):
            
        # print("execute is using", opt3_input)
        # return(param_3_mode, b_mode, c_mode, opt_code)


        # instructions = self.op_code_code_split(int(self.puzzle_input[self.pc]))
        # param_3_mode = instructions[0]
        # b_mode = instructions[1]
        # c_mode = instructions[2]
        # self.op_code = instructions[3]


        # If opt3_no_more_inputs is true then the program has aborted early, and must have been given more inputs,
        if self.op_code3_no_more_inputs == True and len(opt3_input) > 0:
            self.op_code3_no_more_inputs = False
        else: 
            self.pc = 0
        
        # Reset the incrementing pointer for this new execution
        
        

        while self.op_code != 99 and self.op_code3_no_more_inputs == False:
            '''
            1,0,0,3,99
             \ \ \ \ c
              \ \ \ b
               \ \ a
                \ Opt
            '''

            instructions = self.op_code_split(int(self.puzzle_input[self.pc]))
            param_3_mode = instructions[0]
            param_2_mode = instructions[1]
            param_1_mode = instructions[2]
            self.op_code = instructions[3]

            # print(param_3_mode,param_2_mode,param_1_mode,self.op_code,opt3_input)


            # param mode 0 is position mode (value at position)
            # param mode 1 is immediate mode (this position)
            if param_1_mode == 0 and self.op_code != 99:
                param_1 = self.puzzle_input[self.pc+1]
            elif param_1_mode == 1:
                param_1 = self.pc+1
            elif param_1_mode == 2:
                # param_1 = (self.pc+1) + self.relative_base  #[203,0]
                param_1 = self.puzzle_input[self.pc+1]+self.relative_base #[2102]
                # param_1 = self.puzzle_input[(self.pc+1)+self.relative_base] #[203,0]


            # if self.op_code 1
            # add self.pc+1 and self.pc+2 store answer in index self.pc+3
            # skip to self.pc+4
            if self.op_code == 1:
                if param_2_mode == 0:
                    param_2 = self.puzzle_input[self.pc+2]
                elif param_2_mode == 1:
                    param_2 = self.pc+2
                elif param_2_mode == 2:
                    param_2 = self.puzzle_input[self.pc+2]+self.relative_base

                if param_3_mode == 0:
                    param_3 = self.puzzle_input[self.pc+3]
                elif param_3_mode == 1:
                    param_3 = self.pc+3
                elif param_3_mode == 2:
                    param_3 = self.puzzle_input[self.pc+3]+self.relative_base

                self.puzzle_input[param_3] = self.puzzle_input[param_1] + self.puzzle_input[param_2]
                self.pc+=4

            # if self.op_code 2
            # multiply self.pc+1 and self.pc+2 store answer in index self.pc+3
            # skip to self.pc+4
            if self.op_code == 2:
                if param_2_mode == 0:
                    param_2 = self.puzzle_input[self.pc+2]
                elif param_2_mode == 1:
                    param_2 = self.pc+2
                elif param_2_mode == 2:
                    param_2 = self.puzzle_input[self.pc+2]+self.relative_base

                if param_3_mode == 0:
                    param_3 = self.puzzle_input[self.pc+3]
                elif param_3_mode == 1:
                    param_3 = self.pc+3
                elif param_3_mode == 2:
                    param_3 = self.puzzle_input[self.pc+3]+self.relative_base

                self.puzzle_input[param_3] = self.puzzle_input[param_1] * self.puzzle_input[param_2]
                self.pc+=4

            # if self.op_code 3
            # store input in position a
            # skip to self.pc+2
            if self.op_code == 3:
                if len(opt3_input) == 0:
                    # print("We have run out of inputs")
                    self.op_code3_no_more_inputs = True
                    
                else:

                    self.puzzle_input[param_1] = opt3_input.pop(0)
                    self.pc += 2
                    
            
            # if self.op_code 4
            # output the value in position a
            # skip to self.pc+2
            if self.op_code == 4:
                self.last_output.append(self.puzzle_input[param_1])
                    # print(self.last_output)
                # else:
                #    print("Something went wrong and the last output was not 0")
                
                self.pc += 2


            # if self.op_code 5
            # if first param IS NOT 0, set the instruction pointer to the value from the second paramater
            # skip to i= second param
            if self.op_code == 5:
                if param_2_mode == 0:
                    param_2 = self.puzzle_input[self.pc+2]
                elif param_2_mode == 1:
                    param_2 = self.pc+2
                elif param_2_mode == 2:
                    param_2 = self.puzzle_input[self.pc+2]+self.relative_base


                if self.puzzle_input[param_1] != 0: 
                    self.pc= self.puzzle_input[param_2]
                else:
                    self.pc += 3

            # if self.op_code 6
            # if first param IS 0, set the instruction pointer to the value from the second paramater
            # skip to i = second param
            if self.op_code == 6:
                if param_2_mode == 0:
                    param_2 = self.puzzle_input[self.pc+2]
                elif param_2_mode == 1:
                    param_2 = self.pc+2
                elif param_2_mode == 2:
                    param_2 = self.puzzle_input[self.pc+2]+self.relative_base

                if self.puzzle_input[param_1] == 0: 
                    self.pc= self.puzzle_input[param_2]
                else:
                    self.pc+= 3


            # if self.op_code 7
            # if first param is < second param, store '1' in the third param
            # skip to self.pc+4
            if self.op_code == 7:
                if param_2_mode == 0:
                    param_2 = self.puzzle_input[self.pc+2]
                elif param_2_mode == 1:
                    param_2 = self.pc+2
                elif param_2_mode == 2:
                    param_2 = self.puzzle_input[self.pc+2]+self.relative_base

                if param_3_mode == 0:
                    param_3 = self.puzzle_input[self.pc+3]
                elif param_3_mode == 1:
                    param_3 = self.pc+3
                elif param_3_mode == 2:
                    param_3 = self.puzzle_input[self.pc+3]+self.relative_base

                if self.puzzle_input[param_1] < self.puzzle_input[param_2]:
                    self.puzzle_input[param_3] = 1
                else:
                    self.puzzle_input[param_3] = 0
                
                self.pc+= 4


            # if self.op_code 8
            # if fierst param is == second param, store 1 in the third param
            # skip to self.pc+4
            if self.op_code == 8:
                if param_2_mode == 0:
                    param_2 = self.puzzle_input[self.pc+2]
                elif param_2_mode == 1:
                    param_2 = self.pc+2
                elif param_2_mode == 2:
                    param_2 = self.puzzle_input[self.pc+2]+self.relative_base

                if param_3_mode == 0:
                    param_3 = self.puzzle_input[self.pc+3]
                elif param_3_mode == 1:
                    param_3 = self.pc+3
                elif param_3_mode == 2:
                    param_3 = self.puzzle_input[self.pc+3]+self.relative_base

                if self.puzzle_input[param_1] == self.puzzle_input[param_2]:
                    self.puzzle_input[param_3] = 1
                else:
                    self.puzzle_input[param_3] = 0
                
                self.pc+= 4


            # if self.op_code 9
            # adjusts the relative base by the value of its only parameter
            # skip to self.pc+2
            if self.op_code == 9:

                self.relative_base += self.puzzle_input[param_1]
                self.pc+= 2




        # if 99 stop
        return self.last_output


    def op_code_split(self, instruction):
        # Instruction could be anything from 0 to 10000
        #  ABC DE
        #  1002
        # DE - two-digit opcode,      02 == opcode 2
        #  C - mode of 1st parameter,  0 == position mode
        #  B - mode of 2nd parameter,  1 == immediate mode
        #  A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
        # instruction_list = str(instruction).split()
        # ABC DE 
        # 002 03
        # 109 -> 001 09
        instruction_list = [j for j in str(instruction)]

        while len(instruction_list) < 5:
            instruction_list.insert(0,'0')

        opt_code = int(instruction_list[3] + instruction_list[4])

        # return(param_3_mode, param_2_mode, param_1_mode, opt_code)
        return(int(instruction_list[0]), int(instruction_list[1]), int(instruction_list[2]), opt_code)
