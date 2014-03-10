class SuffixTree(object):
    """
    Class suffix tree described here
    """

    def __init__(self, genome):
        self.genome = genome


    def root(self):
        """
        This function returns the root node of object Tree
        @return:
        """
        # method here

    def isleaf(self, v):
        """
        @param v:
        @return:
        """
        # method here

    def child(self, v, c):
        """
        (str, str) -> int
        child returns the node w, that is a child of leaf, v, and the edge
        (v, w) begins with character c, or returns -1 if no such child
        @param v:
        @param c:
        @return:
        """
        # method here

    def sibling(self, v):
        """
        (str) -> int
        sibling returns the next sibling of node, v.
        @param v:
        @return:
        """
        # method here

    def parent(self, v):
        """
        (str) -> int
        parent returns the parent of node v.
        @param v:
        @return:
        """
        # method here

    def edge(self, v, d):
        """
        (str, str) -> str
        edge returns the d-th character of the edge-label of an edge pointing
        to v.
        @param v:
        @param d:
        @return:
        """
        # method here

    def depth(self, v):
        """
        (str) -> int
        depth returns the string-depth node v.
        @param v:
        @return:
        """
        # method here


    def lca(self, v, w):
        """
        (str, str) -> str
        lca returns the lowest common ancestor between nodes v and w
        @param v:
        @param w:
        @return:
        """
