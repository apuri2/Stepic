__author__ = 'apuri'


def oddSum(a, b):
    # Initialize sum at 0
    sumtotal = 0
    for i in range(a, b+1):
        # Use the mod operator to determine if number is odd
        # If the number is odd then it gets added to sum and
        # is equal to the new sum.

        # Because of the way the range generator operates, the
        # last number in the list is not included. This could
        # be problematic if our number is odd, in which case
        # we would unintentionally skip this number in calculating
        # the final sum.
        if i%2 == 1:
            sumtotal += i
    return sumtotal
