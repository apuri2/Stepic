__author__ = 'apuri'

memo = {}

def fib(n, k=1):
    args = (n, k)
    if args in memo:
        return memo[args]  # Aha! We have computed this before!

    # We haven't computed this before, so we do it now
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib(n - 1, k) + k * fib(n - 2, k)
    memo[args] = ans  # don't forget to remember the result!
    return ans
