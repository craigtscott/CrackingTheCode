#! user/bin/env python

"""URLify: Write a method to replace all spaces in a string with '%20'. to run program `python 1.3.py "Mr John Smith    ", 13` 13 is the true length of the string not including the posible blank spaces after"""

import sys

def URLify(string, length):
    spaces = 0
    for i in xrange(length):
        if string[i]  == ' ':
            spaces = spaces + 1


    output = string.replace(' ','%20', spaces)[:length + spaces *  2]
    
    print output
    

if __name__ == "__main__":
    URLify(sys.argv[1],int(sys.argv[2]))

""" The program is determined by the length of the string to be URLifyed O(n) we are also asuming that the input string does not start with a space."""
