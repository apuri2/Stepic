__author__ = 'apuri'

class UkkonenTree(object):
    """
    Uses Ukkonen's algorithm to create a suffix tree in linear time.
    """

    # Constructor
    def __init__(self, string):
        self.string = string

        # Build tree
        while True:
            if not string:
                break

    # Public Methods
    def longComSubString(self, refString):
        """
        Returns the longest common substring of an arbitrarily large string
        str -> str
        @return:
        """
        pass

class Edge(self, firstChar, lastChar):
    """
    Edge class. Contains pointers to the first and last character of string
    """
    self.firstChar = firstChar
    self.lastChar = lastChar

    @property
    def __init__(self):
        assert isinstance(self.lastChar, object)
        return[self.firstChar, self.lastChar]

class Node(self, nodeId=default):
    """
    Node class.
    """