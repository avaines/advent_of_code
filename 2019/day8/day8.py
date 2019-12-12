"""
--- Day 8: Space Image Format ---
The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, 
and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of rebooting! 
It's just waiting for someone to enter a BIOS password. 
The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, 
they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.

Images are sent as a series of digits that each represent the color of a single pixel. 
The digits fill each row of the image left-to-right, then move downward to the next row, 
filling rows top-to-bottom until every pixel of the image is filled.

Each image actually consists of a series of identically-sized layers that are filled in this way. 
So, the first digit corresponds to the top-left pixel of the first layer, 
the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, 
which corresponds to the bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
""" 

import fileinput
from collections import Counter


def part1(puzzle_input, puzzle_width, puzzle_height):

    # An 'image' contains many 'layers', a 'layer' contains many 'row_datas'
    row_data = []
    layer_data = []
    image_data = {}

    # Start a counter
    i = 0
    current_layer = 0

    while i < len(puzzle_input):
        for row in range(0,puzzle_height ):
            for column in range(0,puzzle_width ):
                row_data.append(puzzle_input[i])
                i += 1

            # Row complete
            # Add it to the layer and reset the row_data
            layer_data.append(tuple(row_data))
            row_data = []

        # Layer complete
        # Add it to the image_data, reset the layer_data and increment the layer counter
        image_data[current_layer] = layer_data
        layer_data = []
        current_layer += 1
    
    
    # Picture data has been assembled 
    lowest_zero_count_layer = 0
    lowest_zero_count = 0
    lowest_zero_layer_ones=0
    lowest_zero_layer_twos=0


    for layer in image_data:
        # need to loop through each value
        zeros = 0
        ones = 0
        twos = 0

        for image_rows in image_data[layer]:
            zeros += image_rows.count(0)
            ones += image_rows.count(1)
            twos += image_rows.count(2)
            # print(image_data[layer])

        # sprint("layer:", layer, "| has ", zeros, "zeros")

        if zeros < lowest_zero_count or lowest_zero_count == 0:
            lowest_zero_count = zeros
            lowest_zero_layer_ones = ones
            lowest_zero_layer_twos = twos
            lowest_zero_count_layer = layer        


    return ( lowest_zero_layer_ones * lowest_zero_layer_twos ), image_data




def part2(image_data,puzzle_width,puzzle_height):
    image=""

    #Phase 1: figure out the master image after stacking all the layers
    master_layer_data = []
    # all layers in the image have the same number of rows which will be in puzzle_height
    
    for row in range(0,puzzle_height):
        # looking at the current row

        master_row_data = []
        # 'stack' the layers for the specific row
        for layer in image_data:

            
            #looking at a specific row, check each value in to the master_layer at the same position
            
            pixel_i = 0
            for pixel in image_data[layer][row]:

                # If the master_row_data is not yet built (i.e. this is the first layer), fill it in as a tansparent pixel
                if len(master_row_data)!=puzzle_width:
                    master_row_data.insert(pixel_i,pixel)
                
                # If the current index is at the master_row_data is a 2
                # print(master_row_data[pixel_i])

                if master_row_data[pixel_i] == 2:
                    master_row_data[pixel_i] = pixel

                pixel_i+=1
        
        master_layer_data.append(master_row_data)
        # Next layer

    #Next Row



    # Phase2: Draw the out put

    for layer in master_layer_data:
        # Convert the long list of integers to a string so it can be 'joined' (integers cant be joined)
        map(str, layer)  
        layer = map(str, layer)

        # join the list to make a string then replace the 0's and 1's with symbols
        l=''.join(layer)
        l=l.replace('0', ' ')
        l=l.replace('1','#')


        image+=l+'\n'



    return image




with open('input.txt', 'r') as myfile:
    puzzle_input = [int(x) for x in myfile.read()]

puzzle_width = 25
puzzle_height = 6

p1 = part1(puzzle_input, puzzle_width, puzzle_height)
p2 = part2(p1[1],puzzle_width,puzzle_height)
print("part1:", p1[0])

print(p2)