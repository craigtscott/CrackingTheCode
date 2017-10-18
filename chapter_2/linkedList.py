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



ll1 = linkedList()
ll1.add(3)
ll1.add(5)
ll1.add(7)
print ll1
