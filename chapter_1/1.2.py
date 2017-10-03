#!usr/bin.env python

"""Check Permutation: Given two strings, whrite a method to decide if one is a permutation of the other. """
import sys

def checkPermutation(stringA, stringB):
    if len(stringA) != len(stringB):
        print "False"
        return False
    array = []
    
    if ''.join(sorted(stringA)) == ''.join(sorted(stringB)):
        print "True"
        return True
    else:
        print "False"
        return False
if __name__ == "__main__":
    checkPermutation(str(sys.argv[1]), str(sys.argv[2]))
