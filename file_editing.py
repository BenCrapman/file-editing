#Developed by Ben Chapman
#this program takes an input file, reads it, and copies it to an output file, excluding all uses of the letter e

#create file variable for input data
file_input = open('input.txt', 'r')

#create list that will hold values from file_input
data_input = []
data_output = []

#store file_input into the array
for line in file_input:
	data_input.append(line)

#close the input file, we don't need it anymore
file_input.close()

#print it for testing
print 'input:'
print data_input


#newline
print '\n'

#our output file will include everything in the input file, minus the letter e
#iterate through the input data
for line in data_input:
	#create a temporary variable that stores the current line
	temp_line = ''
	for character in line:
		#iterate through every character in the line string
		if character != 'e':
			#append every character that isn't the letter e to the temp_line variable
			temp_line += character
	#add the de-e'd line to data output
	data_output.append(temp_line)

#create file variable for output data
file_output = open('output.txt', 'w')

#fill output file with the output data array
for line in data_output:
	file_output.write(line)

#close the file
file_output.close()

#print the output contents for debugging
print 'output:'
print data_output

#newline
print '\n'
