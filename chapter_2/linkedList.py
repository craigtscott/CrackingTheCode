class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.nextNode = n
    def getNext(self):
        return self.nextNode
    def setNext(self, n):
        self.nextNode = n
    def getData(self):
        return self.data
    def setData(self, d):
        self.Data = d

class linkedList(object):
    def __init__(self, r = Node):
        self.root = r
        self.size = 0
    def getSize(self):
        return self.size
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, d):
        thisNode = self.root
        prevNode = Node
        while thisNode:
            if thisNode.getData() == d:
                if prevNode:
                    prevNode.setNext(thisNode.getNext())
                else:
                    self.root = thisNode
                    self.size -= 1
                    return True
            else:
                prevNode = thisNode
                thisNode = thisNode.getNext()

        return False
    def find(self, d):
        thisNode = self.root
        while thisNode:
            if thisNode.getData() == d:
                return thisNode
            else:
                thisNode = thisNode.getNext()
        return None                

