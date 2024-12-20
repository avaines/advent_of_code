program = [2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0]
potentials_reg_a = []

def compute_loop_decompiled(reg_a):
    """Run a single loop."""
    reg_b = reg_a % 8 #bst
    reg_b = reg_b ^ 2 #bxl
    reg_c = reg_a // (2**reg_b) #cdv
    reg_b = reg_b ^ 7 #adv
    reg_b = reg_b ^ reg_c #bxl
    return reg_b % 8 #bst

def run_decompiled_compyte(reg_a_candidate, i=0):
    if compute_loop_decompiled(reg_a_candidate) != program[-(i + 1)]:
        return

    if i == len(program) - 1:
        potentials_reg_a.append(reg_a_candidate)
    else:
        for reg_b_candidate in range(8):
            run_decompiled_compyte(reg_a_candidate * 8 + reg_b_candidate, i + 1)

if __name__ == '__main__':
    for reg_a in range(8):
        run_decompiled_compyte(reg_a)

    print(min(potentials_reg_a))
    