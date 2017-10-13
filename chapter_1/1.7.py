# !usr/bin/src python

""" Rotate Matrix NxN matrix by 90 degrees """

import sys
import ast

def rotateMatrix(matrix):
    
    if isinstance(matrix, str):
        matrix = ast.literal_eval(matrix)
    
    if ( len(matrix) == 0 or len(matrix) != len(matrix[0])):
        print False
        return False
    length = len(matrix)
    for layer in range(0, length / 2):
        first = layer
        last = length - 1 - layer
        for index in range(first, last):
            offset = index - first
            top = matrix[first][index]
            matrix[first][index] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last -offset] = matrix[index][last]
            matrix[index][last] = top


    print matrix
if __name__ == "__main__":
    rotateMatrix(sys.argv[1])
    # print "should print: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]"
    # protateMatrix([[1,2,3],[4,5,6],[7,8,9]])
    # print "should print False"
    # rotateMatrix([[1,2],[1,2],[1,2]])
