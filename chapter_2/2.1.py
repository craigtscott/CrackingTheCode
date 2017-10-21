# !usr/bin/src python

"""Remove Dups: write code to remove duplicates from  an unsorted liked list."""
from llist import sllist, sllistnode
from linkedList import Node, linkedList

def removeDups(linkedList):
    
    current = linkedList
    while current != None:
        runner = current
        while runner.getNext() != None:
            if runner.getNext().getData() == current.getData():
                print runner.getNext().getData()
                runner.setNext(runner.getNext().getNext())
                print runner.getNext().getData()
            else:
                runner.setNext(runner.getNext())
        
        current.setNext(current.getNext())

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
    print ll1.getSize()
    removeDups(ll1.getRoot())
    print ll1.getSize()
