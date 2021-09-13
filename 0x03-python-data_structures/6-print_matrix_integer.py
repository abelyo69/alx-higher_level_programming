#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        space = ""
        for col in row:
            print("{:s}{:d}".format(space, col), end="")
            space = " "
        print()
