# Project Euler: Smallest Multiple
# Status: COMPLETE

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# NOOT: This was done in a very inefficient way, taking over 30 minutes to compute.
#       Consider Daniel Cone's advice: Start by multiplying 1, 2, then find gcd.
#       of 2, 3, multiple your answer by 3/gcd, keep going forth... (?)

def divisible(number):
    # Checks if the number is evenly divisible by all the numbers from 1 to 20

    for i in range(1, 21):
        if (number % i != 0):
            # print("Yeah,", number, "ain't the number.")
            return False

    return True

def main():

    number = 2520

    found = False

    while (not found):
        if (divisible(number)):
            strNumber = str(number)
            print("The smallest positive number that is evenly divisible by all the numbers from 1 to 20 is:", strNumber + ".")
            found = True
        number += 1

    return 0

main()
