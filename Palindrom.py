def check_palindrom(s1):
    left = 0
    right = len(s1) - 1
    while left < right:
        if s1[left] != s1[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == '__main__':
    print(check_palindrom('viren'))
    print(check_palindrom('madam'))