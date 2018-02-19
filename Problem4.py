# Euler Project: Largest Palindrome Project
# Status: INCOMPLETE

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# NOOT: This is incomplete as I have not made a function to find the product
#       of those two 3-digit numbers yet.

class Stack:
     # This class is from the Interactive Python website
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def main():

    product = Stack()

    digit = input("Please enter an integer: ")

    index = 0

    # Push the digits
    while (index < len(digit)):
        product.push(digit[index])
        index += 1

    # Assign the digits
    sixthDigit = product.pop()
    fifthDigit = product.pop()
    fourthDigit = product.pop()
    thirdDigit = product.pop()
    secondDigit = product.pop()
    firstDigit = product.pop()

    if (checkPalindrome(firstDigit, secondDigit, thirdDigit, fourthDigit, fifthDigit, sixthDigit) is True): # Checks if the product is a palindrome
        print("The largest palindrome made from the product of two 3-digit numbers is:", digit)

def checkPalindrome(firstDigit, secondDigit, thirdDigit, fourthDigit, fifthDigit, sixthDigit):

    if (firstDigit != sixthDigit) or (secondDigit != fifthDigit) or (thirdDigit != fourthDigit):
        return False
    return True

main()
