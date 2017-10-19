# !usr/bin/src python


""" Delete Middle Node: Implement an algorythem to delete a node in the middle ex. a>b>c>d>e>f into a>b>d>e>f """

from llist import sllist, sllistnode
from linkedList import Node, linkedList

def delMidNode( linkedListNode):
    if linkedListNode == None or linkedListNode.getNext() == None:
        print False
        return False
    next = linkedListNode.getNext()
    linkedListNode.setData(next.getData())
    linkedListNode.setNext(next.getNext())
    return True

if __name__ == "__main__":
    ll1 = linkedList()
    ll1.add(1)
    ll1.add(2)
    ll1.add(3)
    ll1.add(4)
    ll1.add(5)
    ll2 = sllist([])
    delMidNode(ll1.find(2))
