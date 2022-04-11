"""
Author: Jakub Kupkovic
Date: 11.4.2022

Description: Program runs multiple generators and switches between them.
"""

def generator(count,i):
    """
    Generator returns formated string of its id and time yielded
    :param count: number of max yields
    :param i: identificator
    :return: string message
    """
    for n in range(1, count+1):
        yield "Task : {} returns {}".format(i,n)

def scheduler(sizes):
    """
    create generators with set max yields
    :param sizes: max yields of each generator
    :return: generators
    """
    gens = []
    for i, size in enumerate(sizes):
        gens.append(generator(size, i))
    return gens


def main():
    generators = scheduler([3,2,1])
    pass

if __name__ == "__main__":
    main()