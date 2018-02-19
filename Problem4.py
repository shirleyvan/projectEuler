# Euler Project: Largest Palindrome Project
# Status: COMPLETE

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

class Palindrome:
    # Has methods from a class Stack

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def findLargestProduct(self, digit):
        # Checks for all the products from 999 multipled by 999 decreasing,
        # stopping when a palindrome has been found

        for x in range(999, 900, -1):
            for y in range(999, 900, -1):
                digit = x * y
                if (self.checkPalindrome(digit)):
                    strDigit = str(digit)
                    print("The largest palindrome made from the product of two 3-digit numbers is:", strDigit + ".")

                    return 0

    def checkPalindrome(self, digit):
        # Checks if the product is a palindrome

        index = 0
        strDigit = str(digit)

        # Push the digits into a stack
        while (index < len(strDigit)):
            self.push(strDigit[index])
            index += 1

        # Assign the digits by popping them off the stack
        sixthDigit = self.pop()
        fifthDigit = self.pop()
        fourthDigit = self.pop()
        thirdDigit = self.pop()
        secondDigit = self.pop()
        firstDigit = self.pop()

        if (firstDigit != sixthDigit) or (secondDigit != fifthDigit) or (thirdDigit != fourthDigit):
            return False

        return True

def main():
    # Note that the product of two 3-digit numbers is 6-digits long

    product = Palindrome()

    digit = 0 # Because I had to send an integer value to product.findLargestProduct

    product.findLargestProduct(digit)

main()
