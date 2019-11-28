#2.4
#Partition: Write code to partition a linked list around a value x, 
#such that all nodes less than x come before all nodes greater than 
#or equal to x. lf x is contained within the list, the values of x only
#need to be after the elements less than x (see below).The partition element 
#x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

#assuming no cycles

from random import randrange

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    @classmethod
    def genList(cls, len :int, max: int):
        l = SLinkedList()
        l.headval = Node(randrange(max))
        it = l.headval

        for i in range(len):
            n = Node (randrange(max))
            it.nextval = n
            it = it.nextval
        return l

    def printList(self):
        s = ""
        it = self.headval
        while (it != None):
            s += str((it.dataval)) + ", "
            it = it.nextval
        print(s)

#just return a node :) 
def partition (h:SLinkedList, val:int):
    lHead = None
    rHead = None 
    l = None
    r = None
    i = h.headval
    while (i != None):
        if (i.dataval < val):
            if (l == None):
                l = i
                lHead = i
            else: 
                l.nextval = i
                l = i
        else:
            if (r == None):
                r = i
                rHead = i
            else:
                r.nextval = i
                r = i 
        i = i.nextval
    l.nextval = rHead
    r.nextval = None
    rtn = SLinkedList()
    rtn.headval = lHead
    return rtn

list1 = SLinkedList.genList(10, 10)

list1.printList()

r = partition(list1, 5)

r.printList()