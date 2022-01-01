def balance_check(str1):
    openb = ['[', '{', '(']
    closeb = [']', '}', ')']

    stack = []
    for s in str1:
        if s in openb:  # Push index of opening bracket to stack
            stack.append(openb.index(s) + 1)
        elif s in closeb:  # Pop from stack
            if closeb.index(s) + 1 == stack[len(stack) - 1] and stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


# resp = balance_check('[](){([[[]]])}')
# resp = balance_check('()(){]}')
# resp = balance_check('[}')
# resp = balance_check('[](){([[[]]])}(')
# resp = balance_check('[{{{(())}}}]((()))')
resp = balance_check('[[[]])]')

if resp:
    print("String is Balanced !!")
else:
    print("String is NOT Balanced !!")
