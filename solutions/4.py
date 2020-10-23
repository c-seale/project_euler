"""
    Project Euler: Largest palindrome product (Problem 4)


    A palindromic number reads the same both ways. The largest palindrome made from the product of
    two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

NUMBER_OF_DIGITS = 3


def is_palindrome(string: str) -> bool:
    for i in range(0, len(string) // 2):
        if string[i] != string[(i + 1) * -1]:
            return False
    return True


start = int('1' + '0' * (NUMBER_OF_DIGITS - 1))
end = int('9' * NUMBER_OF_DIGITS)

largest_palindrome = (0, 0, 0)
for i in range(start, end + 1):
    for j in range(start, end + 1):
        product = i * j
        if is_palindrome(str(product)):
            if product > largest_palindrome[2]:
                largest_palindrome = (i, j, product)

print(largest_palindrome)
