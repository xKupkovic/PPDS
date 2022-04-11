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

def main():

    pass

if __name__ == "__main__":
    main()