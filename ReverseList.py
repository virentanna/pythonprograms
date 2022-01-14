# This program reverses a given list

list1 = [1, 8, 3, 2, 9]

first_index = 0
last_index = len(list1) - 1

while first_index < last_index:
    list1[first_index], list1[last_index] = list1[last_index], list1[first_index]
    first_index += 1
    last_index -= 1

print(list1)
