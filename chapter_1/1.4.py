#! user/bin/env python

"""palindrome permutation: given a string, write a function to check if it is a permutation of a plaindreome. to run program enter `python 1.4.py sting` into the terminal"""
import sys

def palPer(strings):
    string = "".join(strings)
    list = [0] * 26
    oddCount = 0
    for l in string:
        index = ord(l.lower())-97
        if list[index] == 0:
            list[index] = 1
            oddCount = oddCount + 1
        else:
            list[index] = 0
            oddCount = oddCount - 1
            
    if oddCount > 1:
        print "False"
        return False

    print "True"
    return True

if __name__ == "__main__":
    palPer(sys.argv[1:])


""" Big O(n) determined by the length of string input I decided to make spaces not part of the panendrome"""
