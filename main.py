"""
Author: Jakub Kupkovic
Date: 25.4.2022

Description: Bruteforce search for matrix solution
"""
import random

from numba import cuda
import math


def random_bit():
    """
    Returns random bit
    :return: random bit
    """
    return random.randint(0, 1)


def generate_random_bit_matrix(n, m):
    """
    Generates random bit matrix
    :param n: number of columns
    :param m: number of rows
    :return: 2d (n*m) array of bits
    """
    return [[random_bit() for i in range(n)] for j in range(m)]


@cuda.jit
def my_kernel_3D(io_array, n, m):
    """
    Brute forces all vectors to find solution
    :param io_array: 2D array of bits
    :param n: number of columns
    :param m: number of rows
    """
    x, y = cuda.threadIdx.x, cuda.threadIdx.y
    z = cuda.threadIdx.z + cuda.blockDim.z * cuda.blockIdx.z


def main():
    """
    Function searches all vectors for solution
    """
    n, m = 10, 8
    mat = generate_random_bit_matrix(n, m)

    # Threads:256
    threads_per_block = (16, 16, 2)
    blocks_per_grid = (math.ceil(n / threads_per_block[0]),
                       math.ceil(m / threads_per_block[1]),
                       math.ceil((2 ** n) / threads_per_block[2]))

    my_kernel_3D[blocks_per_grid, threads_per_block](mat, n, m)

    print(mat)
    pass


if __name__ == "__main__":
    main()
