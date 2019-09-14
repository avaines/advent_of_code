"""
To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID 
containing exactly two of any letter and then separately counting those with exactly three of any letter. 
You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:
- abcdef contains no letters that appear exactly two or three times.
- bababc contains two a and three b, so it counts for both.
- abbcde contains two b, but no letter appears exactly three times.
- abcccd contains three c, but no letter appears exactly two times.
- aabcdd contains two a and two d, but it only counts once.
- abcdee contains two e.
- ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. 
Multiplying these together produces a checksum of 4 * 3 = 12.
"""

import fileinput
puzzle_input = list(fileinput.input("day2.txt"))

# puzzle_input = ("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab")

def part1():
    num_of_doubles = 0 
    num_of_tripples = 0

    # For each line in the input file
    for line in puzzle_input:

        tmp_doubles = False
        tmp_tripples = False
        # for each unique letter in the line
        for letter in list(set(line)):
            if line.count(letter) == 2:
                tmp_doubles = True
            
            if line.count(letter) == 3:
                tmp_tripples = True

        if tmp_doubles == True:
            num_of_doubles +=1
            tmp_doubles = False
        if tmp_tripples == True:
            num_of_tripples +=1
            tmp_tripples = False
    print("doubles:",num_of_doubles, "|", "tripples:",num_of_tripples)
    return num_of_doubles * num_of_tripples



# puzzle_input = ("abcde", "fghij", "klmno", "pqrst" ,"fguij", "axcye", "wvxyz")

import Levenshtein 
def part2():

    # for each line in the the puzzle
    for line in puzzle_input:

        # comparte it to each line
        for target_line in puzzle_input:
            # Standard altorythm for doing this the levenshtein one (i think)
            # If its only 1 letter distant
            if ( Levenshtein.distance(line, target_line) ) == 1:

                print( line.strip(), "and", target_line.strip(), "are 1 letter distant")
                
                # Create variables for each matching line as a stripped list ([a,b,c])
                line_l = list(line.strip())
                target_line_l = list(target_line.strip())

                # Create empty list for matching characters
                matching = []

                # for each each index in the length of the string for the matching line
                # check if the same index on the other matching line is the same,
                # if it is add the character at that index to the 'matching' list
                for i in range( len( line_l )):
                    if line_l[i] == target_line_l[i]:
                        matching.append( line_l[i] )
                    
                # return the list of matching characters but joined with an empty character
                return "".join(matching)
                




print(part1())
print(part2())