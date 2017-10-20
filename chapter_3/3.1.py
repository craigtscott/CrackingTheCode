# !usr/bin/src python

"""Three in One: Describe how you could use a single array to implement three stacks. """

class ThreeStacks(object):
    def __init__(self, stackSize):
        self.values = [None] * stackSize * 3
        self.stackSize = stackSize

        self.indexHash = {0: [0, self.stackSize], 1: [self.stackSize, self.stackSize * 2 ], 2: [self.stackSize * 2, self.stackSize * 3]}

    def push(self, stackNum, value):
        print self.indexHash
        if self.indexHash[stackNum][0] == self.indexHash[stackNum][1]:
            print "FULL"
            return False
        else:
            self.values[self.indexHash[stackNum][0]] = value
            self.indexHash[stackNum] = [self.indexHash[stackNum][0] + 1, self.indexHash[stackNum][1]]
            return True
    def pop(self, stackNum):
        if self.indexHash[stackNum][1] - self.indexHash[stackNum][0] == self.stackSize:
            print "empty"
            return False
        else:
            print self.indexHash[stackNum][0]            
            self.values[self.indexHash[stackNum][0] - 1] = None
            self.indexHash[stackNum] = [self.indexHash[stackNum][0] - 1, self.indexHash[stackNum][1]]
            print self.indexHash[stackNum]
    def printStacks(self):
        print self.values
        return True


multi = ThreeStacks(3)
multi.push(0,1)
multi.push(0,2)
multi.push(0,3)
multi.pop(0)
multi.push(1,4)
multi.printStacks()
multi.pop(1)
multi.printStacks()
