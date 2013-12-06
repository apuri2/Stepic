#!/usr/bin/env python


class Node():
    """
    A Node in a suffix tree. Contains the location. -1 indicates there are no parent Nodes.

    Creates a parent Node unless modified.
    """
    def __init__(self):
        self.loc = -1
         = []

class Edge():
    def __init__(self):
    self.s = []

def Kmer(k, dna):
    """
    kmer(num, str) -> list(str)
    """
    winlen = k

