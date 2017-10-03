#!usr/bin.env python

"""Check Permutation: Given two strings, whrite a method to decide if one is a permutation of the other. To run this program run `$python 1.2.py stringA stringB` """

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

""" Pythons sorting performance in O(n lon n) so this is what we should expect from the function """
