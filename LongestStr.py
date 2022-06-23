def lengthOfLongestSubStr(s1):
    tempstr=[]
    length=0
    for letter in s1:
        if letter in tempstr:
            if length < len(tempstr):
                length = len(tempstr)
            tempstr.clear()

        tempstr.append(letter)

    if length < len(tempstr):
        return len(tempstr)
    else:
        return length

def LongestStr(s):
    if len(s) == 0:
        return "Empty String..."

    s = list(s)
    tempstr = []
    maxlen=0
    idx=0

    while idx < len(s):
        if s[idx] in tempstr:
            maxlen = max(maxlen,len(tempstr))
            tempstr = []
            s = s[s.index(s[idx]) + 1:]
            idx=0

        tempstr.append(s[idx])
        idx += 1

    return max(maxlen,len(tempstr))


if __name__ == '__main__':
    # print(LongestStr('dvdf'))
    print(LongestStr('abcabcbb'))
    # print(LongestStr('bbbbb'))
    # print(LongestStr('pwwkew'))
    # print(LongestStr(' '))
    # print(LongestStr('viren'))
