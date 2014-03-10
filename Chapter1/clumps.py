f = open("dataset_4_4.txt", "r")
genome = f.readline()
genome = genome.rstrip()
variables = f.readline()
variables = variables.split()
k = int(variables[0])
L = int(variables[1])
t = int(variables[2])
f.close()

def clumps(genome, k, L, t):
    """
    Script finds k -mers occuring at least t times, in windows of length L,
    for an entire genome
    @param genome:
    @param k:
    @param L:
    @param t:
    @return:
    """

    # Create dictionary of
    # and a list of frequent patterns
    words = {}
    freqpatterns = []

    # Populate the dictionary
    j = 0

    # Loop until we reach the end of the genome
    while j < len(genome):

        # Loop a little at a time
        for i in range(j, L - k + j + 1):
            word = genome[i:i+k]
        
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        j = i + k - 1
        i = 0
    # If word appears at least t times, then return an array of all the words
    for kmer, freq in words.items():
        if freq >= t:
            freqpatterns.append(kmer)

    return ' '.join(map(str, freqpatterns))

