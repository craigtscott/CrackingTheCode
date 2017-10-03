#!/usr/bin/env python

"""1.1.py: Is Unique: Implemment an algorythem to determin if a string has all unique characters. What if you cannot use additional data structures? """
import sys

def isUnique(string):
    dict = {}
    for letter in string:
        if letter in dict:
            print "False"
            return False 
        dict[letter]=True
    
    print "True"
    return True

if __name__ == "__main__":
    isUnique(sys.argv[1])

""" Time complexity is O(n) n being the length of the string"""
