def strCompress(s):
    temp = []
    final = []

    if len(s.strip()) == 0 :
        return 'String is Blank...'

    for char in s:
        if len(temp) == 0 or temp[-1] == char:
            temp.append(char)
        else:
            final.append(temp[-1] + str(len(temp)))
            temp.clear()
            temp.append(char)
    final.append(temp[-1] + str(len(temp)))

    return ''.join(final)

if __name__ == '__main__':
    print(strCompress('    '))
    # print('AABBCC' + '---->' + strCompress('AABBCC'))
    # print('AAABCCDDDDD' + '---->' + strCompress('AAABCCDDDDD'))
    print('AAAaaaBCCddDDDDD' + '---->' + strCompress('AAAaaaBCCddDDDDD'))