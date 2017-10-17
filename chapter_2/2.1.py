# !usr/bin/src python

"""Remove Dups: write code to remove duplicates from  an unsorted liked list."""
from llist import sllist, sllistnode

def removeDups(linkedList):
    
    if (linkedList.first is None):
        return

    seenHash = {}
    current = linkedList.first
    touched = set([current.value])
    while current.next:
        print seenHash
        print current.next.value
        if current.next.value in seenHash:
            current = current.next
            linkedList.remove(current) 
        else:
            seenHash[current.next.value] = True
            current = current.next
    return linkedList

if __name__ == "__main__":
    linkedList = sllist([1,2,3,2,4,3,5,4,6,7])
    print linkedList
    removeDups(linkedList)
    print linkedList

    ll2 = sllist([1,2,3,4,5,5])
    print ll2
    removeDups(ll2)
    print ll2

    ll3 = sllist([])
    removeDups(ll3)

    ll4 = sllist([1,1,1,2,3,3])
    print ll4
    removeDups(ll4)
    print ll4
