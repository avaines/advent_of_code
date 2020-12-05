"""
task summary/notes
"""

import fileinput
import collections
import re

def part1(passport_list, debug):
    valid_passports = 0

    for passport in passport_list:
        if debug: print(passport)

        if "byr" in passport:
            if debug: print ("\tbirth year found")
        else:
            continue

        if "iyr" in passport:
            if debug: print ("\tissue year found")
        else:
            continue

        if "eyr" in passport:
            if debug: print ("\texpiration year found")
        else:
            continue

        if "hgt" in passport:
            if debug: print ("\height found")
        else:
            continue

        if "hcl" in passport:
            if debug: print ("hair colour found")
        else:
            continue

        if "ecl" in passport:
            if debug: print ("eyecolor found")
        else:
            continue

        if "pid" in passport:
            if debug: print ("passport id found")
        else:
            continue

        if "cid" in passport:
            if debug: print ("country id found")
        else:
            if debug: print ("country id NOT found")
            # continue

        valid_passports +=1

    return valid_passports


def part2(passport_list, debug):
    valid_passports = 0
    total_passports = 0

    for passport in passport_list:
        total_passports +=1

        if debug: print(passport)

        if "byr" in passport:
            if debug: print ("\tbirth year found")
            if 1920 <= int(passport['byr']) <= 2002:
               if debug: print ("\t\tbirth year valid")
            else:
                if debug: print ("\t\tbirth year INVALID")
                continue
        else:
            continue

        if "iyr" in passport:
            if debug: print ("\tissue year found")
            if 2010 <= int(passport['iyr']) <= 2020:
               if debug: print ("\t\tissue year valid")
            else:
                if debug: print ("\t\tissue year INVALID")
                continue
        else:
            continue

        if "eyr" in passport:
            if debug: print ("\texpiration year found")
            if 2020 <= int(passport['eyr']) <= 2030:
               if debug: print ("\t\texpiration year valid")
            else:
                if debug: print ("\t\texpiration year INVALID")
                continue
        else:
            continue

        if "hgt" in passport:
            if debug: print ("\ttheight found")

            if re.search('[0-9]{1,3}cm', passport['hgt']):
                if debug: print ("\t\theight is in CM")
                if 150 <= int(passport['hgt'].replace('cm','')) <= 193:
                    if debug: print ("\t\t\theight is valid")
                else:
                    if debug: print ("\t\t\the height is INVALID")
                    continue

            elif re.search('[0-9]{1,2}in', passport['hgt']):
                if debug: print ("\t\tHeight is in IN")
                if 59 <= int(passport['hgt'].replace('in','')) <= 76:
                    if debug: print ("\t\t\theight is valid")
                else:
                    if debug: print ("\t\t\theight is INVALID")
                    continue
            else:
                if debug: print ("\t\theight INVALID")
                continue
        else:
            continue

        if "hcl" in passport:
            if debug: print ("\thair colour found")
            # a # followed by exactly six characters 0-9 or a-f.
            if re.search('#[a-f0-9]{6}', passport['hcl'] ):
                if debug: print ("\t\thair colour is valid")
            else:
                if debug: print ("\t\thair colour is INVALID")
                continue
        else:
            continue

        if "ecl" in passport:
            if debug: print ("eyecolor found")
            if any(passport['ecl'] in s for s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] ):
               if debug: print ("\t\teye colour valid")
            else:
                if debug: print ("\t\teye colour INVALID")
                continue
        else:
            continue

        if "pid" in passport:
            if debug: print ("\tpassport id found")
            # a nine-digit number, including leading zeroes.
            if re.search('[0-9]{9}$', passport['pid'] ):
                if debug: print ("\t\tthe passport id is valid")
            else:
                if debug: print ("\t\tthe passport id is INVALID")
                continue
        else:
            continue

        if "cid" in passport:
            if debug: print ("country id found")
        else:
            if debug: print ("country id NOT found")
            # continue

        if debug: print ("\tPASSPORT VALID")
        valid_passports +=1
        # print(passport['byr'],", ", passport['iyr'],", ", passport['eyr'],", ", passport['hgt'],", ", passport['hcl'],", ", passport['ecl'],", ", passport['pid'])

    return valid_passports, total_passports-valid_passports

def chunk_batch_file(puzzle_input):
    list_of_objects = []
    map_of_passport_objects=[]

    for line in puzzle_input.split("\n\n"):
        # Split the file on the new lines
        list_of_objects.append(line)

    for line in list_of_objects:
        # With each chunk in the batch file, get rid of the remaining new lines, then break that list/dict appart on the : and create key value pairs
        line = line.replace("\n", " ")
        chunk = dict(s.split(":") for s in line.split(" ") )
        map_of_passport_objects.append(chunk)

    return map_of_passport_objects


# puzzle_input = list(fileinput.input('sample1.txt'))
with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read()

passport_list = chunk_batch_file(puzzle_input)

p1 = part1(passport_list, False)
p2 = part2(passport_list, False)

print("#############################################################")
print("Part1: Valid:", p1 )
print("Part2: Valid:", p2[0], "| Invalid:", p2[1] )