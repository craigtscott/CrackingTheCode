# !usr/bin/src python

""" Return Kth to Last: implement an algoruthem to find the kth to last element of a singly linked list"""

from llist import sllist, sllistnode

def returnKth(linkedList, k):
    if len(linkedList) < k:
        return
    print "hello"

if __name__ == "__main__":
    ll1 = sllist([])
    returnKth(ll1, 4)
    returnKth(ll1, 0)
