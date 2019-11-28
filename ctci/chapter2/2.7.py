#2.7
#Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
#Return the inter- secting node. Note that the intersection is defined based on reference, 
#not value. That is, if the kth node of the first linked list is the exact same node (by reference) 
#as the jth node of the second linked list, then they are intersecting.

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

#walk both lists, if you end up at the same spot they are the same
def intersect(l1: SLinkedList, l2: SLinkedList) -> bool:
    s = set()

    itr = l1.headval
    while (itr.nextval != None):
        s.add(itr)
        itr = itr.nextval
    itr2 = l2.headval
    while (itr2.nextval != None):
        if (itr2 in s):
            return True
        itr2 = itr2.nextval
    return itr == itr2

list1 = SLinkedList.genList(10, 10)
list2 = SLinkedList.genList(5, 10)

print(intersect(list1, list2))

list2.headval.nextval = list1.headval.nextval.nextval.nextval

list1.printList()
list2.printList()

print(intersect(list1, list2))