# Euler Project: Problem3.py
# Status: INCOMPLETE

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# NOOT: This solution is incomplete as I cannot generate primes correctly as of yet.

def main():

    n = int(input("Please enter an integer: "))

    prime = []

    # Generates a list of prime numbers up to the input
    isPrime(n, prime)

    if (len(prime) == 0): # If the input is a prime itself
        print("The largest prime factor of", n, "is", str(n) + ".")
    else:
        largestPrimeFactor = str(prime.pop())
        print("The largest prime factor of", n, "is", largestPrimeFactor + ".")

def isPrime(n, prime):
    # Generates all the prime numbers up to n

    for number in range(3, n, 2):
        if (n % number == 0):
            prime.append(number)

    ############################################################################
    print("This is the list of primes: ", prime)
    ############################################################################

    return prime

main()
