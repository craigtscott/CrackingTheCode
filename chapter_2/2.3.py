# !usr/bin/src python

""" Delete Middle Node: Implement an algorythem to delete a node in the middle ex. a>b>c>d>e>f into a>b>d>e>f """

from llist import sllist, sllistnode

def delMidNode( linkedListNode):
    if linkedListNode == None or linkedListNode.next == None:
        print False
        return False
    next = linkedListNode.next
    linkedListNode.next = next.next
    return True

if __name__ == "__main__":
    ll1 = sllist([1,2,3,4,5,6])
    ll2 = sllist([])
    delMidNode(ll1.nodeat(2))
