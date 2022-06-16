def ArrayPair_Sum(arr,k):
    if len(arr) < 2:
        print("Array size is less than 2...")
        return

    sol = []
    for idx,num in enumerate(arr):
        if k - num in arr[idx+1:]:
            if (num,k-num) not in sol:
                sol.append((num,k-num))
    print(sol)


def pair_sum(arr, k):
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

    # FOR TESTING
    # return len(output)
    # Nice one-liner for printing output
    print('\n'.join(map(str,list(output))))

if __name__ == '__main__':
    ArrayPair_Sum([1,3,2,2,6,4,5],7)
    # pair_sum([1, 3, 2, 2, 6, 4, 5], 7)