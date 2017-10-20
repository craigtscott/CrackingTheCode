# !usr/bin/src python

"""Three in One: Describe how you could use a single array to implement three stacks. """

class ThreeStacks(object):
    def __init__(self, stackSize):
        self.values = [None] * stackSize * 3
        self.stackSize = stackSize

        self.stack0Bottom = 0
        self.stack0Top = self.stack0Bottom + self.stackSize

        self.stack1Bottom = self.stack0Top
        self.stack1Top = self.stack1Bottom + self.stackSize

        self.stack2Bottom = self.stack1Top
        self.stack2Top = self.stack2Bottom + self.stackSize

        self.stackIdx = [0, self.stackSize, self.stackSize * 2]

    def push(self, stackNum, value):
        if False:#isFull(stackNum):
            print "FULL"
            return False
        else:
            self.values[self.stackIdx[stackNum]] = value
            self.stackIdx[stackNum] =  self.stackIdx[stackNum] + 1
            return True
    #def isFull(n):
     #   return False

    def printStacks(self):
        print self.values
        return True


multi = ThreeStacks(3)
multi.push(0,1)
multi.push(1,2)
multi.push(2,3)
multi.printStacks()
