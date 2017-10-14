# !usr/bin/src python 

""" Zero Matrix: if a element of a NxM matrix is 0 all in its row and collum is set to 0 """
import sys
import ast

def zeroMatrix(matrix):
    if isinstance(matrix, str):
        matrix = ast.literal_eval(matrix)
    print "initial:" 
    print matrix
    row = [False]*len(matrix)
    col = [False]*len(matrix[0])

    for index in range(0, len(matrix)):
        for jndex in range(0, len(matrix[0])):
            if matrix[index][jndex] == 0:
                row[index] = True
                col[jndex] = True
    
    print row
    print col
    for index in range(0, len(row)):
        if row[index] == True:
            zeroRow(matrix, index)
    for index in range(0, len(col)):
        if col[index] == True:
            zeroCol(matrix, index)

    print "return:"
    print matrix

def zeroRow(matrix, index):
    for jndex in range(0, len(matrix[0])):
        matrix[index][jndex] = 0
    return matrix

def zeroCol(matrix, jndex):
    for index in range(0, len(matrix)):
        matrix[index][jndex] = 0
    return matrix
if __name__ == "__main__":
    # zeroMatrix(sys.argv[1])
    print "should be [[0,0],[0,3]]"
    zeroMatrix([[0,1],[2,3]])
    print "should be [[1,0,1],[0,0,0][1,0,1]]"
    zeroMatrix([[1,1,1],[1,0,1],[1,1,1]])
