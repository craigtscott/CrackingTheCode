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

    print matrix
if __name__ == "__main__":
   # rotateMatrix(sys.argv[1])
   print "should print: [[3,6,9],[2,5,8],[1,4,7]]"
   rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])
   print "should print False"
   rotateMatrix([[1,2],[1,2],[1,2]])
