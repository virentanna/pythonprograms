def balance(exp):
    opened = ['(','{','[']
    closed = [')','}',']']
    pair = [ ('(',')'), ('{','}'), ('[',']')]

    if len(exp) % 2 != 0 :
        return False

    stack = []
    for char in exp:
        if char in opened:
            stack.append(char)
        else:
            if (stack[-1],char) in pair:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    print(balance('[](){([[[]]])}}'))