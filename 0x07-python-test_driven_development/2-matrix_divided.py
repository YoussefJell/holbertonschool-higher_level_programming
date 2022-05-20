#!/usr/bin/python3
"""2-matrix_divided
this module has the function matrix_divided
"""


def matrix_divided(matrix, div):
    """matrix_divided
    this will divide a matrix over the div argument

        matrix must be a matrix (list of lists) of integers/floats
        Each row of the matrix must have the same size
        div must be a number
        and you cannot divide by zero

    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    for elem in matrix:
        if type(elem) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for e in matrix[:]:
        new_matrix.append(list(map(lambda num: round((num / div), 2), e)))
    return new_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6, 7]
]
print(matrix_divided(matrix, 4))
print(matrix)
