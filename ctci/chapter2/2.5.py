#2.5
#Sum Lists: You have two numbers represented by a linked list,
#where each node contains a single digit. The digits are stored
#in reverse order, such that the 1's digit is at the head of the list. 
#Write a function that adds the two numbers and returns the sum as a linked list.

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


def addList(l1:SLinkedList, l2:SLinkedList) -> SLinkedList:
    l = SLinkedList()
    i = l1.headval
    j = l2.headval

    li = Node()
    l.headval = li
    carry = 0
    while (i != None or j != None or carry != 0):
        n = Node(None)
        if (i == None and j == None):
            n.dataval = (carry) % 10
            carry = (carry) // 10
        elif (i == None):
            n.dataval = (j.dataval + carry) % 10
            carry = (j.dataval + carry) // 10
        elif (j == None):
            n.dataval = (i.dataval + carry) % 10
            carry = (i.dataval + carry) // 10
        else:
            n.dataval = (j.dataval + i.dataval + carry) % 10
            carry = (j.dataval + i.dataval + carry) // 10

        if (li.dataval == None):
            li.dataval = n.dataval
        else:
            li.nextval = n
            li = n
        if (i != None):
            i = i.nextval
        if (j != None):
            j = j.nextval

    return l




list1 = SLinkedList.genList(randrange(10), 10)
list2 = SLinkedList.genList(randrange(10), 10)

list1.printList()
list2.printList()

list3 = addList(list1, list2)

list3.printList()