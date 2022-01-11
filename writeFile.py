# Program to read the input file and write the reversed file to output file

# Code reads the input file
with open('testinput.txt', 'r') as fi:
    data = fi.readlines()
    data[-1] += '\n'

# Code writes the output file
with open('testoutput.txt', 'w') as fo:
    for line in reversed(data):
        fo.write(line)
