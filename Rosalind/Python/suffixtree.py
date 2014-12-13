__author__ = 'Apurv Puri'


class UkkonenTree(object):
    """
    Uses Ukkonen's algorithm to create a suffix tree in linear time.
    Suffix Tree is a collection of Edges and Nodes to
    """

    def __init__(self, genome):
        self.genome = genome
        self.nodes = [Node()]       # Collection of nodes in tree, also initializes the root node
        self.edges = {}             # Collection of edges in tree

        # Build tree
        for index, char in enumerate(genome):
            self._add_Prefix(index)


    def _add_Prefix(self, index):
        """
        Main method to create the suffix tree.
        """
        # Always start at the root node?
        last_node_index = -1
        while True:
            edge = Edge()

class Edge(object):
    """
    Edge class. Contains pointers to the first and last character of string
    """
    def __init__(self, first_nuc_index, last_nuc_index, from_node, to_node):
        """
        """
        self.first_nuc_index = first_nuc_index
        self.last_nuc_index = last_nuc_index
        self.from_node = from_node
        self.to_node = to_node

    @property
    def length(self):
        return self.last_nuc_index - self.first_nuc_index


class Node(object):
    """
    Node class
    """
    def __init__(self, suffix_node=-1):
        self.suffix_node = suffix_node

    def is_root(self):
        return self.suffix_node == -1