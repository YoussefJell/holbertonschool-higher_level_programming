#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        newer_matrix = []
        for i in range(len(matrix)):
            new_matrix = []
            for j in range(len(matrix[i])):
                new_matrix.append(matrix[i][j] ** 2)
            newer_matrix.append(new_matrix)
        return newer_matrix
