import re


def subs(handle):
    """
    (str) -> None

    Function subs prints the locations of the motif specified in the DNA in question
    """
    f = open(handle, 'r')

    motif = "CTTGATCAT"
    dna = f.readline()

    # Remove any trailing whitespace
    dna = dna.rstrip()
    motif = motif.rstrip()

    # Use a list comprehension using Regular Expressions
    # Use a look ahead assertion when using Reg Exp

    forward = '(?='
    back = ')'
    patt = forward + motif + back
    zeroindex = [m.start() for m in re.finditer(patt, dna)]

    print(' '.join(map(str, zeroindex)))
