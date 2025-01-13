#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Function Description:
        The function computes the factorial of the provided number `n`. The factorial
        of a number is the product of all positive integers less than or equal to `n`.
        It uses a recursive approach where `n! = n * (n-1)!`. For `n = 0`, the result is 1.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given number `n`. If `n` is 0, returns 1 as `0! = 1`.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: factorial is n * factorial of (n-1)
        return n * factorial(n-1)

# Get the input from the command-line arguments, calculate factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
