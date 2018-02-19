# Project Euler: Multiples of 5 and 3

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():

    multipleOf3 = 0
    multipleOf5 = 0
    sumOf = 0

    listOfValidNumber = []

    n = int(input("Please input a number: "))

    for naturalNumber in range(1, n):
        multipleOf3 = naturalNumber / 3
        multipleOf5 = naturalNumber / 5

        if (multipleOf3 % 1 == 0) or (multipleOf5 % 1 == 0):
            # Checks if the naturalNumber is an integer
            listOfValidNumber.append(naturalNumber)

    for validNumber in listOfValidNumber:
        # Computes the sum of validNumber
        sumOf += validNumber

    print(sumOf)

main()
