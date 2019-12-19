"""
task summary/notes
""" 

import fileinput
import collections

# puzzle_input = list(fileinput.input('sample1.txt'))
with open('input.txt', 'r') as myfile:
    puzzle_input = myfile.read().split("\n")


def part1(orbits):
    '''
            G - H       J - K - L
           /           /
    COM - B - C - D - E - F
                \
                 I
    '''

    for i in range(len(orbits)):
        orbits[i] = orbits[i].split(")")


    all_orbits_list =[]

    # for each orbit get the parent and child of the orbits and put them in the all_orbits_list
    for left_plannet in range(len(orbits)):

        for right_planet in range(len(orbits[left_plannet])):
            
            all_orbits_list.append(orbits[left_plannet][right_planet])


    # get rid of any duplicates by turning it in to a set
    planets = list(set(all_orbits_list))

    if 'COM' in planets: 
        planets.remove('COM')

    #total count of all direct and indirect orbits, find and count the orbits
    orbit_count = 0
    for planet in planets:
        orbit_count += count_orbits(orbits,planet, 0)

    return orbit_count,0



#recursive function: find and count all direct AND indirect orbits going backwards
def count_orbits(orbits, planet, count):
    for i in orbits:
    
        local_count = count
        end_check = i[0]
        planet_check = i[1]
    
        if(planet_check==planet):
            if(end_check!="COM"):
                local_count += 1
                returnValue = count_orbits(orbits,end_check,local_count)
            else:
                local_count +=1
                returnValue = local_count
            
    return returnValue


def part2(orbits):
    '''
            G - H       J - K - L - YOU
           /           /
    COM - B - C - D - E - F
                \
                 I - SAN
    '''

    # stuff_dict = defaultdict(list)


    def track_orbit(start,end):
        print(orbits )

        for orbit in orbits:
            if orbit == start:
                print(orbit)

        print()

    
    track_orbit('YOU','END')



    print()



    return




p1 = part1(puzzle_input)
print(p1[0])
# print(part2(p1[1]))