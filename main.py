"""
Author: Jakub Kupkovic
Date: 25.4.2022

Description: Bruteforce search for matrix solution
"""
from numba import cuda
import math

def generate_random_bit_matrix(n,m):
    """
    Generates random bit matrix
    :param n: number of columns
    :param m: number of rows
    :return: 2d (n*m) array of bits
    """
    return [[i for i in range(n)] for j in range(m)]


def main():
    print(cuda.gpus)
    pass

if __name__ == "__main__":
    main()