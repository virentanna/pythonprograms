# This program reverses a given list

list1 = [1, 8, 3, 2, 9]

firstindex = 0
lastindex = len(list1) - 1

while firstindex < lastindex:
    list1[firstindex], list1[lastindex] = list1[lastindex], list1[firstindex]
    firstindex += 1
    lastindex -= 1

print(list1)
