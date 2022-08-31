#!/usr/bin/python3

"""a function that computes the square
value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    new_mat = [i[:] for i in matrix]
    for y in range(len(new_mat)):
        for z in range(len(new_mat[y])):
            new_mat[y][z] *= new_mat[y][z]
    return new_mat
