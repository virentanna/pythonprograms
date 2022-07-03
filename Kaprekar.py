def FindMinMax(num):
    max = [x for x in str(num)]
    if len(max) < 4:
        for idx in range(len(max),4):
            max.append('0')

    max.sort(reverse=True)

    min = [x for x in str(num)]
    if len(min) < 4:
        for idx in range(len(min), 4):
            min.append('0')

    min.sort()

    return (int(''.join(max).zfill(4)),int(''.join(min).zfill(4)))

def Kapricon(num,idx):
    if num == 6174:
        print("Number reaches the Kaprekar 6174 in steps : ",idx)
        steps = idx
        return
    else:
        idx += 1
        max,min = FindMinMax(num)
        Kapricon(max-min,idx)

if __name__ == '__main__':
    num=5134

    Kapricon(5134,0)

