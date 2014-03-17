__author__ = 'apuri'

# This code is functional with files of much larger sizes.

import itertools
import sys

with open('input.txt') as f:
    sys.stdout.writelines(itertools.islice(f, 1, None, 2))
