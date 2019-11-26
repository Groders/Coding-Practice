#2.1

#Remove Dups: Write code to remove duplicates from an unsorted li nked list. 
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?
#   n^2 sollution? don't see a better way, might check hint later
#   apperntly you can inplace merge sort in O(nlog(n)) 
#   then you can remove duplicates in one pass, so better than n^2

from random import randrange


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


def remDup (h: SLinkedList)-> SLinkedList:
    s = set()
    i = h.headval
    p = h.headval
    while (i != None):
        if (i.dataval in s):
            if (i == h.headval):
                h.headval = i.nextval
                p = i.nextval
                i = i.nextval
            else:
                p.nextval = i.nextval
                i = i.nextval
        else:
            s.add(i.dataval)
            #remove
            p = i
            i = i.nextval
    return h


list1 = SLinkedList()
list1.headval = Node(1)
it = list1.headval

#generate linked list
for i in range(100):
    n = Node (randrange(10))
    it.nextval = n
    it = it.nextval

it = list1.headval
while (it != None):
    print(it.dataval)
    it = it.nextval

print("Remove")
remDup(list1)
it = list1.headval
while (it != None):
    print(it.dataval)
    it = it.nextval
