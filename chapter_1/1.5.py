# !user/bin/src python

""" One Away: There are three types of edits that can be performed on a string: insert a character, remove charater or replace charater. check to see if they are one edit away"""
import sys

def oneAway(stringA, stringB):
    dif =abs( len(stringA) - len(stringB))
    if dif > 1:
        print "False"
        return False



if __name__ == "__main__":
    oneAway(sys.argv[1], sys.argv[2])
