# Euler Project: Problem3.py

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def main():

    indice = 1
    n = int(input("Please enter an integer: "))
    actualN = n

    prime = []
    largestPrime = []

    # Generates a list of prime numbers up to the input
    isPrime(n, prime)

    # Checks if the prime numbers are divisible by the input
    for number in prime:
        if (number % n == 0):
            n = number / n
        largestPrime.append(number)

    ############################################################################
    print("This is the list of primes that actually work: ", largestPrime)
    ############################################################################

    numberOfElements = len(largestPrime)

    if (numberOfElements == 2): # If the input is a prime itself
        print("The prime factor of", actualN, "is 1 and", str(actualN) + ".")
    else:
        largestPrime.remove(1) # Remove 1 and itself because the input is not prime
        largestPrime.pop()
        print("The prime factors of", actualN, "are")
        while (indice < numberOfElements):
            print("," + str(largestPrime[indice]))
            indice += 1
        print(".")

def isPrime(n, prime):
    # Generates all the prime numbers up to and including n

    for number in range(1, n + 1):
        if (n % number == 0):
            prime.append(number)

    ############################################################################
    print("This is the list of primes: ", prime)
    ############################################################################

    return prime

main()
