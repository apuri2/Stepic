#!/usr/bin/env python

def kmerbrute(k, dna):
    """
    kmerbrute(num, str) -> list(str)

    Brute force method to compute all kmers [(Composition)k of (Text)]
    """
    cleandna = dna.strip()