__author__ = 'apuri'

def stringFinder(string, a, b, c, d):
     magic = [string[a:b+1], string[c:d+1]]
     return ' '.join(magic)