# !usr/bin/src python

"""Remove Dups: write code to remove duplicates from  an unsorted liked list."""
from llist import sllist, sllistnode
from linkedList import Node, linkedList

def removeDups(linkedList):
    
    if (linkedList.getRoot() is None):
        return

    seenHash = {}
    current = linkedList.getRoot()
#    touched = set([current.value])
    while current != None:
        runner = current
        while runner.getNext() != None:
            print runner.getData()
            print runner.getNext().getData()
            print current.getData()
            if runner.getNext().getData() == current.getData():
                runner.setNext(runner.getNext().getNext())
            else:
                current = current.getNext()
            #current.setNext(current.getNext())
            #linkedList.remove(current) 
        #else:
            #seenHash[current.getData()] = True
            #current = current.getNext()

    return linkedList

if __name__ == "__main__":
    ll1 = linkedList()
    ll1.add(1)
    ll1.add(2)
    ll1.add(3)
    ll1.add(2)
    ll1.add(4)
    ll1.add(3)
    ll1.add(5)
    ll1.add(4)
    ll1.add(6)
    ll1.add(7)
    print "remoxe##############"
    removeDups(ll1)

