#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        size = len(i)
        last = 1
        for i2 in i:
            if size == last:
                print(f"{i2}", end='')
            else:
                print(f"{i2} ", end='')
            last = last + 1
        print("")
