# Program to find the factorial of a given number

def factorial(num):
    if (num <= 0):
        return "Enter Valid number..."

    fact = 1
    while num > 1:
        fact *= num
        num -= 1

    return fact

# Function to find factorial using recursion
def factorial_rec(num):

    if num == 1:
        return num
    else:
        return num * factorial_rec(num-1)


if __name__ == '__main__':
    print(factorial_rec(4))