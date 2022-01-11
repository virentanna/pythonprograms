# fi = open('testinput.txt')

# To read the entire file at one shot
# print(fi.read())

# To read the initial 10 chars of input file
# print(fi.read(10))

# # To read the file line by line using READLINE() method
# line = fi.readline()
# while line != '':
# This will cut the New line char while printing However it will cut last valid char of last line too
#     print(line[:-1])
#     line = fi.readline()

# Read the file using READLINES() method
with open('testinput.txt') as fi:
    for line in fi.readlines():
        if line[-1] == '\n':
            print(line[:-1])
        else:
            print(line)



