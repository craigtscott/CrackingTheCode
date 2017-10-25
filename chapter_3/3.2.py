# !usr/bin/src python

"""Stack Min: How would you design a stack which, in addition to push a pop, has a function min which returns the  minimum element? Push, pop and min should all operate in O(1) time. """

class StackWithMin(object):
    def __init__(self):
        self.minimum = None
        self.values = [None]*10
        self.index = 0


    def push(self, value):
        if self.minimum > value or self.minimum == None:
            self.minimum = value
        
        self.values[self.index] = value
        self.index = self.index + 1
        print  self.minimum
        print self.values

    def getMin(self):
        min = self.values[0]
        for i in range (1,10):
            if self.values[i] == None:
                return min
            if self.values[i] < min :
               min = self.values[i]
        return min

    def pop(self):
        if self.index > 0:
            self.index = self.index - 1
            popped = self.values[self.index]
            self.values[self.index] = None
        if popped == self.minimum:
            self.minimum = self.getMin()
        print self.minimum
        print self.values
min = StackWithMin()
min.push(5)
min.push(4)
min.push(3)
min.pop()
min.pop()

""" to run $ pyhton 3.2.py

the push is O(1) pop is O(n) but needs revision"""
