
# For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.
# In this example, the resulting frequency is 3.

# Here are other example situations:

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6

import fileinput

frequencies = list(fileinput.input())


def part1():
    # Treat each entry as integer and add them together
    return sum(map(int, frequencies))


def part2():

    # Initial frequency
    frequency_value = 0

    # List to store whitnessed values
    seen = {frequency_value}


    # loop through the list of frequencies, but keep doing it until we find one, we might need to go over the list a couple of times 
    # (which is why the while true is here)
    while True:
        for frequency in frequencies:   

            # add the next value
            frequency_value += int(frequency)

            # does the current value match something in the witnessed list
            if frequency_value in seen:
                # yes, it has already been seen
                return frequency_value

            else:
                # no, add the current value to the list that have alrady been seen
                seen.add(frequency_value)



print("Part 1:", part1())
print("Part 2: Found two occurences of", part2())
