#!/usr/local/bin/python3
from sys import argv

MATRIX_HEADER = r"$$\begin{Bmatrix}"
MATRIX_FOOTER = r"\end{Bmatrix}$$"
SOFT_TAB      = "   "

'''
   a & b \\
   c & d
'''

def generate_matrix(x, y):
    # the matrix represented as a string
    matrix_string = ""
    matrix_string += MATRIX_HEADER + '\n'

    for dimension in range(y-1):
        matrix_string += SOFT_TAB
        for dimension in range(x-1):
            matrix_string += 'a & '
        matrix_string += "a \\" + '\n'
    matrix_string += "a" + '\n'

    matrix_string += MATRIX_FOOTER + '\n'

    return matrix_string


def main():
    # TODO type conversion exception handling
    dimension_x = int(argv[1])
    dimension_y = int(argv[2])
    print(generate_matrix(dimension_x, dimension_y))


main()
