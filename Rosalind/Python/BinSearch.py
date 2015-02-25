__author__ = 'apuri'


def preprocess(rawFile):
    """
    file -> list, list

    Preprocesses a raw file for testing binary search algorithm.
    @param rawFile:
    @return:
    """
    data = []
    with open(rawFile) as rawText:
        for rawData in rawText.readlines():
            data.append(rawData.split())

        sortNumList = data[2]
        randNumList = data[3]

        sortList = [int(num) for num in sortNumList]
        randList = [int(num) for num in randNumList]

    return sortList, randList


def binsearch(sortList, randList):
    """
    list, list -> list

    Given two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers
    from −10^5 to 10^5 and a list of m integers −10^5 ≤ k1,k2,…,km ≤ 10^5, for
    each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

    @param sortList:
    @param randList:
    @return:
    """
    # First, lets initialize a list with length of randList
    indexMatch = []

    for item in randList:
        begIndex = 0
        endIndex = len(sortList)

        while True:
            midIndex = (begIndex + endIndex) // 2

            if sortList[midIndex] < item:
                begIndex = midIndex + 1
            else:
                endIndex = midIndex - 1

            if begIndex > endIndex:
                break

        if begIndex == len(sortList) or sortList[begIndex] != item:
            indexMatch.append(-1)
        else:
            indexMatch.append(begIndex + 1)

    return indexMatch

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()