# !usr/bin/src python

"""Stack Min: How would you design a stack which, in addition to push a pop, has a function min which returns the  minimum element? Push, pop and min should all operate in O(1) time. """

import imp
my_module = imp.load_source('ThreeStacks', '3.1.py')
class StackWithMin(ThreeStacks):
    def __init__(self, stackSize):
        self.minimum = [None]*3
        self.stacks = ThreeStacks.__init__(self, stackSize)

    def push(self, stackNum, value):
        if self.minimum[stackNum] > value:
            self.minimum[stackNum] = value
        self.stacks.push(stackNum, value)
        print  self.minimum[stackNum]



min = StackWithMin(ThreeStacks(9))
min.push(0,5)
min.push(0,4)
