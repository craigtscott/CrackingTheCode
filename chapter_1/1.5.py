# !user/bin/src python

""" One Away: There are three types of edits that can be performed on a string: insert a character, remove charater or replace charater. check to see if they are one edit away"""
import sys

def oneAway(stringA, stringB):
    dif =abs( len(stringA) - len(stringB))
    if dif > 1:
        print "False"
    
    if dif == 1:
        for string in [stringA, stringB]:
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
    oneAway(sys.argv[1], sys.argv[2])
