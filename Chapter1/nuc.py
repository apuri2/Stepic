#! /usr/bin/env python


f = open('reverse_complement_data.txt', 'r')
DNA = f.read()

def compstrand(strand):
    return strand.translate(str.maketrans('TAGCtagc', 'ATCGATCG'))


revcDNA = compstrand(DNA)


print(revcDNA[::-1])