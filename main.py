"""
Author: Jakub Kupkovic
Date: 25.4.2022

Description: Bruteforce search for matrix solution
"""
import random

import numpy
from numba import cuda, b1
import math



# TPB = 64
@cuda.jit
def my_kernel_3D(io_array, expected_vector, cached_matrix, result_vectors):
    """
    Brute forces all vectors to find solution
    :param result_vectors: returned results
    :param cached_matrix: allocated matrix writen to in block
    :param expected_vector: expected vector
    :param io_array: 2D array of bits

    """
    # sA = cuda.shared.array(shape=(TPB, TPB), dtype=b1)
    x = cuda.threadIdx.x
    y = cuda.threadIdx.y
    m,n = io_array.shape

    tz = cuda.threadIdx.z
    z = tz + cuda.blockDim.z * cuda.blockIdx.z
    cached_matrix[y][x] = x+y
    if x < n and y < m and tz == 0:
        cached_matrix[y][x] = io_array[y][x] ^ ((z >> y) & 1)

    cuda.syncthreads()

    if x == 0:
        bit_sum = 0
        for i in range(y):
            bit_sum += cached_matrix[y][i]
        cached_matrix[y][n + tz] = bit_sum % 2

    cuda.syncthreads()

    if x == 0 and y == 0:
        equal = 0
        for i in range(y):
            if cached_matrix[i][n + tz] == expected_vector[0][y]:
                equal = 1

        if equal == 0:
            for i in range(y):
                result_vectors[y][tz] = ((z >> y) & 1)
    cuda.syncthreads()


def main():
    """
    Function searches all vectors for solution
    """
    n, m = 16, 16
    mat = numpy.random.randint(0, 2, size=(m,n), dtype=int)
    cached_array = numpy.zeros((m,n +2), dtype=int)

    expected_vector = numpy.ones((m,1), dtype=int)
    result_vectors = numpy.full((m,2), -1, dtype=int)

    # Threads:256
    threads_per_block = (16, 16, 1)
    vector_num = 2 ** n
    print(vector_num)
    blocks_per_grid = (math.ceil(n / threads_per_block[0]),
                       math.ceil(m / threads_per_block[1]),
                       math.ceil(vector_num / threads_per_block[2]))

    d_mat = cuda.to_device(mat)
    d_cache = cuda.to_device(cached_array)
    d_expected = cuda.to_device(expected_vector)
    d_results = cuda.to_device(result_vectors)

    my_kernel_3D[blocks_per_grid, threads_per_block](d_mat,
                                                     d_cache,
                                                     d_expected,
                                                     d_results)

    print(d_results.copy_to_host())

    pass


if __name__ == "__main__":
    main()
