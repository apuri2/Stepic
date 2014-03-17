__author__ = 'apuri'

def oddSum(a, b):
    # Initialize sum at 0
    sum = 0
    for i in  range(a, b):
        # Use the mod operator to determine if number is odd
        # If the number is odd then it gets added to sum and
        # is equal to the new sum
        if i%2 == 1:
            sum = sum + i
    return sum
