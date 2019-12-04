"""
task summary/notes
""" 

import fileinput

puzzle_input = (240920,789857)
# puzzle_input = (111111,111223)

def part1(low, high):
    matches=[]
    matches_found = 0

    for pass_candidate in range(low,high+1):

        match_duplicates=0
        match_increases=True

        for j in range(0, len(str(pass_candidate))-1):
            
            current_number = str(pass_candidate)[j]
            next_number = str(pass_candidate)[j+1]
            
            # Two adjacent digits are the same (like 22 in 122345).
            if current_number == next_number:
                match_duplicates+=1

            # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

            if int(current_number) > int(next_number):
                match_increases = False

        if match_duplicates > 0 and match_increases == True:
            # print(pass_candidate)
            matches.append(pass_candidate)
            matches_found +=1

    return matches_found, matches


def part2(p1_matches):
    matches = 0
    
    for pattern in p1_matches:
        tripple = ""
        double = ""

    # Does it have a 2 run of numbers?
        #for j in range(0, len(str(pattern))-1):


    # Does it have a 3 run of numbers?
        for j in range(0, len(str(pattern))-1):
            
            # does it also have a 3 run of some different numbers?
            if j < len(str(pattern))-2:
                if str(pattern)[j] == str(pattern)[j+1] and str(pattern)[j] == str(pattern)[j+2]:
                    tripple = str(pattern)[j]
            
            if str(pattern)[j] == str(pattern)[j+1]:
                if str(pattern)[j] != tripple:
                    double = str(pattern)[j]
            

        if (tripple != "" and double != "") or (tripple == "" and double != ""):
            matches +=1

    return matches


p1_ans = part1(puzzle_input[0],puzzle_input[1])
print("Part 1 :", p1_ans[0])

print("Part 2 :", part2(p1_ans[1]))
