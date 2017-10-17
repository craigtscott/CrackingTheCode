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
        if current.next.value in seenHash:
           linkedList.remove(current.next) 
        else:
            seenHash[current.next.value] = True
            current = current.next
    return linkedList

if __name__ == "__main__":
    linkedList = sllist([1,2,3,2,4,3,5,4,6,7])
    print linkedList
    removeDups(linkedList)
    print linkedList
