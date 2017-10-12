# !usr/bin/src python

""" Rotate Matrix NxN matrix by 90 degrees """

import sys
import ast

def rotateMatrix(matrix):
    matrix = ast.literal_eval(matrix)
    
    if len(matrix) == 0:
        print False


if __name__ == "__main__":
    rotateMatrix(sys.argv[1])
