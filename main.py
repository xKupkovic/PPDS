"""
Author: Jakub Kupkovic
Date: 25.4.2022

Description: Implementation of matrix number operation on CUDA
"""
from numba import cuda

def main():
    print(cuda.gpus)
    pass

if __name__ == "__main__":
    main()