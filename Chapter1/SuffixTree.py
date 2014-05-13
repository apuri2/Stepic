__author__ = 'apuri'


class SuffixTree(object):
    """
    Suffix Tree
    Generates a suffix tree of input string, s. The tree can be queried for a variety of features.
    """
    class Node(object):
        def __init__(self, label):
            self.label = label  # Label on each path leading to this node.
            self.out = {}   # Outgoing edges; maps characters to nodes.

    def __init__(self, s):
        """
        Make suffix tree, without suffix links, from s in quadratic time and linear space
        """
        s += '$'
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)

        # Add the rest of the suffixes from longeset to shortest
        for i in range(1, len(s)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    label = child.label
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    k = j+1
                    while k-j < len(label) and s[k] == label[k-j]:
                        k += 1
                    if k-j == len(label):
                        cur = child  # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cexist, cnew = label[k-j], s[k]
                        # create “mid”: new node bisecting edge
                        mid = self.Node(label[:k-j])
                        mid.out[cnew] = self.Node(s[k:])
                        # original child becomes mid’s child
                        mid.out[cexist] = child
                        # original child’s label is curtailed
                        child.label = label[k-j:]
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def followPath(self, s):
        """ Follow path given by s.  If we fall off tree, return None.  If we
            finish mid-edge, return (node, offset) where 'node' is child and
            'offset' is label offset.  If we finish on a node, return (node,
            None). """
        cur = self.root
        i = 0
        while i < len(s):
            c = s[i]
            if c not in cur.out:
                return (None, None) # fell off at a node
            child = cur.out[s[i]]
            label = child.label
            j = i+1
            label = label
            while j-i < len(label) and j < len(s) and s[j] == label[j-i]:
                j += 1
            if j-i == len(label):
                cur = child # exhausted edge
                i = j
            elif j == len(s):
                return (child, j-i)  # exhausted query string in middle of edge
            else:
                return None, None  # fell off in the middle of the edge
        return cur, None  # exhausted query string at internal node

    def hasSubstring(self, s):
        """ Return true iff s appears as a substring """
        node, off = self.followPath(s)
        return node is not None

    def hasSuffix(self, s):
        """ Return true iff s is a suffix """
        node, off = self.followPath(s)
        if node is None:
            return False  # fell off the tree
        if off is None:
            # finished on top of a node
            return '$' in node.out
        else:
            # finished at offset 'off' within an edge leading to 'node'
            return node.label[off] == '$'