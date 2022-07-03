# SORT the array by shifting all EVEN number to left while ODD number to the left

# Algorithm : If we get an odd number, pop it and append it to the list
def EvenOddSort(arr):
    idx = 0
    length = len(arr)
    while idx < length:
        if arr[idx] % 2 != 0:
            arr.append(arr[idx])
            arr.pop(idx)
            length -= 1
        else:
            idx += 1
    return arr

# Algorithm : Look for an even number, shuffle it with index 0 
def EvenOddSort01(arr):

    for idx,num in enumerate(arr):      
        if num % 2 == 0:
            arr[idx],arr[0] = arr[0],arr[idx] 

    return arr

if __name__ == '__main__':
    myarray = [11,43,24,21,31,78,5,4,12,44]
    print(myarray)
    print(EvenOddSort(myarray))
    print(EvenOddSort01(myarray))
