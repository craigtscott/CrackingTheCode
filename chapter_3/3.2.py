# !usr/bin/src python

"""Stack Min: How would you design a stack which, in addition to push a pop, has a function min which returns the  minimum element? Push, pop and min should all operate in O(1) time. """

from ThreeStacks import ThreeStacks
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



min = StackWithMin()
min.push(5)
min.push(4)
