# Anagram Check
# 'viren' is anagram of 'nevir'

def anagram_check(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) == len(s2) and s1.sort() == s2.sort():
        return True
    return False


print(anagram_check('viren', 'neriv'))
