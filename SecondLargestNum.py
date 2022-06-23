def Find_Second_Largest(arr):
    max=0
    max02=0

    for num in arr:
        if num > max:
            max02=max
            max = num
        elif num > max02:
            max02 = num

    return (max,max02)

if __name__ == '__main__':
    print(Find_Second_Largest([33,1,22,6,4,30,5,15]))
    print(Find_Second_Largest([1, 22, 6, 4, 30, 5, 33, 15]))
    print(Find_Second_Largest([33,1,22,6,4,30,5,45]))
    print(Find_Second_Largest([33, 44, 22, 6, 4, 30, 5, 15]))
    print(Find_Second_Largest([77, 66, 22, 6, 4, 30, 5, 15]))