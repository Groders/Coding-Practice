#2.8
#Loop Detection: Given a circular linked list, implement an 
#algorithm that returns the node at the beginning of the loop.
#DEFINI TION
#Circular linked list: A (corrupt) linked list in which a node's next 
#pointer points to an earlier node, so as to make a loop in the linked list.

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

    def detectCycle(self) -> Node:
        fast = self.headval
        slow = self.headval
        #go until they meet in the cycle
        while (fast != None and slow != None and fast.nextval != None):
            fast = fast.nextval.nextval
            slow = slow.nextval
            if (slow == fast):
                break
        
        if (slow == None or fast == None):
            return None
        
        #they meet in the cycle the same distance away from the start of loop 
        #as the start of loop to start of linked list
        slow = self.headval
        while (slow != fast):
            slow = slow.nextval
            fast = fast.nextval
        return fast

list1 = SLinkedList.genList(10, 10)
list1.printList()

print(list1.headval.nextval.nextval.nextval.nextval.nextval.nextval.nextval.nextval.nextval.dataval)
print(list1.headval.nextval.nextval.nextval.nextval.nextval.dataval)
list1.headval.nextval.nextval.nextval.nextval.nextval.nextval.nextval.nextval.nextval = list1.headval.nextval.nextval.nextval.nextval.nextval
print(list1.detectCycle().dataval)