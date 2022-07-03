import collections
def Finder(arr1,arr2):
    d=collections.defaultdict(int)

    for num in arr2:
       d[num] += 1

    for num in arr1:
        if d[num] == 0:
            print(num,end=" ")

def Finder01(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num

    return result

if __name__ == '__main__':
    Finder01([1,2,3,4,5,6,7],[3,7,2,1,4])
