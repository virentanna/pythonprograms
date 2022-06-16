# ------------------------------------------------------------------
# Program to find first 100 prime numbers and add them to list
# ------------------------------------------------------------------

#Function to check if a given number is prime or not
def is_prime(num):
    for x in range(2,num):
        if num % x == 0:
            return False
    return True

#Function to add first 100 prime numbers to a list
def list_of_100_primes():
    prime_arr=[]
    num = 1
    while len(prime_arr) < 10:
        if is_prime(num):
            prime_arr.append(num)
        num += 1

    return prime_arr

# main() function to start the execution
if __name__ == '__main__':
    print(list_of_100_primes())
