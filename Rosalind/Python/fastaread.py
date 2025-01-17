def fastaread(handle):
    """
    file -> list, list
    Reads a fasta file and returns all the ids and sequences corresponding to those ids
    inside an array.

    TODO:
    Need to figure out how to return generators instead to save space for really large
    files.
    """
    # Initialize some arrays to return first
    fastaid = []
    seqarray = []

    # Open file
    f = open(handle, 'r')

    # First while True:/Break idiom to pass any and all blank spaces
    while True:
        line = f.readline()
        if not line:
            return
        if line[0] is '>':           # If we find a fasta id however, then we break
            break

    # Now we'll start our other while True:/Break idiom
    # This one will find the fasta record, put that record in an array.
    # Then until the next record or end of file is encountered, it will
    # read in all the lines and return that sequence

    while True:
        if not line.startswith('>'):
            raise ValueError("Records in FASTA files should start with > character")

        title = line[1:].rstrip()
        fastaid.append(title)

        # Initialize our seqdata variable. This one will store one single sequence.
        seqdata = []

        line = f.readline()

        # This second while True:/Break idiom extracts the sequence data.
        while True:
            if not line:
                break
            if line[0] == '>':       # Check to see if we're onto the next record
                break
            seqdata.append(line.rstrip())
            line = f.readline()

        # Take the data in seqdata and join it together and add to the seqarray
        nts = ''.join(seqdata).replace(" ", "").replace("\r", "")
        seqarray.append(nts)

        # If we're at the end of the document we'll go ahead and return our array
        # of ids and sequences
        if not line:
            return fastaid, seqarray

    f.close()