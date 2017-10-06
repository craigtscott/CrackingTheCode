# !usr/bin/src python

""" String Compression: implement a method to perform basic sting compression using counts of repeated charaters. e.g. aabcccccaaa ===> a2b1c5a3 """
import sys

def stringCompression(string):
    output = ""
    tempLetter = string[0]
    counter = 0
    for i in range ( 1, len( string)):
        print i-1
        print string[i-1]
        if string[i - 1] == tempLetter:
            counter = counter + 1
        if  string[i] != string[i-1]:
            output = output + string[i-1] + str(counter)
            counter = 0
            print output
            tempLetter = string[i]
    output = output + tempLetter + str(counter)
    print output


if __name__ == "__main__":
    stringCompression(sys.argv[1])

""" Big 0(n) where n is string length stil could use some refractoring """
