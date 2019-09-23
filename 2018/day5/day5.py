

import fileinput

puzzle_file = list(fileinput.input('day5/day5.txt')[0])


def part1(puzzle_input):
	
	match_found = True
	
	
	while match_found == True:
		for i in range(len(puzzle_input)):
		#	print('.', end='')
			match_found = False
				
			#print(i, 'of', len(puzzle_input), ': ', puzzle_input)
				
			if (puzzle_input[i]).isupper():	
						
				if i != len(puzzle_input)-1:			
					if (puzzle_input[i+1]).islower() and puzzle_input[i+1] == (puzzle_input[i]).lower():
						match_found = True
					
					#	print ('A found', puzzle_input[i], 'behind',  puzzle_input[i+1], 'at', i)
					
			#			print('removing', puzzle_input[i])
						puzzle_input.pop(i)
					
				#		print('removing', puzzle_input[i])
						puzzle_input.pop(i)	
					
						#print('back to top of loop')
						break
	
									
				if i != 0:
					if (puzzle_input[i-1]).islower() and puzzle_input[i-1] == (puzzle_input[i]).lower():
						match_found = True
						#print('previous letter is lower but same')
					
						
	#					print ('B found', puzzle_input[i], 'in front of',  puzzle_input[i-1], 'at', i)
			#			print('removing', puzzle_input[i])
						puzzle_input.pop(i)
					
			#			print('removing', puzzle_input[i])
						puzzle_input.pop(i)	
					
						#print('back to top of loop')
						break
						
				
			else:
				
				if i != len(puzzle_input)-1:
					
					if (puzzle_input[i+1]).isupper() and puzzle_input[i+1] == (puzzle_input[i]).upper():
						match_found = True
						#print('next letter is lower but same')
						
						
			#			print ('C found', puzzle_input[i], 'behind',  puzzle_input[i+1], 'at', i)
		#				print('removing', puzzle_input[i])
						puzzle_input.pop(i)
					
				#		print('removing', puzzle_input[i])
						puzzle_input.pop(i)	
					
	
						#print('back to top of loop')
						break
			
							
				if (puzzle_input[i-1]).isupper() and puzzle_input[i-1] == (puzzle_input[i]).upper():
					match_found = True
					#print('previous letter is lower but same')
					
					
			#		print ('D found', puzzle_input[i], 'in front of',  puzzle_input[i-1], 'at', i)
			#		print('removing', puzzle_input[i])
					puzzle_input.pop(i)
					
				#	print('removing', puzzle_input[i])
					puzzle_input.pop(i)	
	
					#print('back to top of loop')
					break
			
	
	
	#print('dabCBAcaDA <- should be')
	return len(puzzle_input)
	
import string

def part2(puzzle_list):
	
	best_count=0
	
	for letter in list(string.ascii_lowercase):
		print('checking for instances of', letter)
		puzzle_check=list()
		puzzle_check[:] = (value for value in puzzle_list if value != letter.upper() and value != letter.lower())
		#print(puzzle_check)
		last_count = part1(puzzle_check)
		print(last_count)
		if last_count < best_count or best_count == 0:
			best_count = last_count
	
	return best_count

# print('part1:', part1(puzzle_file))
print('part2:', part2(puzzle_file))