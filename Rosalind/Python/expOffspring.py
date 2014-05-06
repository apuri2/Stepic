__author__ = 'apuri'


def expOffSpring(population):
    probability = [1, 1, 1, 3 / 4, 1 / 2, 0]
    listExpOffSpring = []

    for i in range(len(population)):
        listExpOffSpring.append(population[i] * probability[i])

    return 2 * sum(listExpOffSpring)
