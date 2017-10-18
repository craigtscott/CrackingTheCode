# !usr/bin/src python

""" Return Kth to Last: implement an algoruthem to find the kth to last element of a singly linked list"""

from llist import sllist, sllistnode

def returnKth(linkedList, k):

    pointer1 = linkedList.first
    pointer2 = linkedList.first

    for index  in range(0, k):
        if pointer1 == None:
            return False
        pointer1 = pointer1.next

    while pointer1 != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    print pointer2
    return pointer2

if __name__ == "__main__":
    ll1 = sllist([])
    ll2 = sllist([5,4,3,2,1])
    returnKth(ll1, 4)
    returnKth(ll2, 3)
    returnKth(ll2, 4)
    returnKth(ll2, 5)
    returnKth(ll2, 6)
    returnKth(ll2, 0)
