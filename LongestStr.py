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

if __name__ == '__main__':
    # print(lengthOfLongestSubStr('abcabcbb'))
    # print(lengthOfLongestSubStr('bbbbb'))
    # print(lengthOfLongestSubStr('pwwkew'))
    # print(lengthOfLongestSubStr(' '))
    # print(lengthOfLongestSubStr('viren'))
    print(lengthOfLongestSubStr('dvdf'))