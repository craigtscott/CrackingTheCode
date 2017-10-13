# !usr/bin/src python 

""" Zero Matrix: if a element of a NxM matrix is 0 all in its row and collum is set to 0 """
import sys
import ast

def zeroMatrix(matrix):
    if isinstance(matrix, str):
        matrix = ast.literal_eval(matrix)
    print matrix

if __name__ == "__main__":
    # zeroMatrix(sys.argv[1])
    print "should be [[0,0],[0,3]]"
    zeroMatrix([[0,1],[2,3]])
    print "should be [[1,0,1],[0,0,0][1,0,1]]"
    zeroMatrix([[1,1,1],[1,0,1],[1,1,1]])
