#2.3
#Delete Middle Node: Implement an algorithm to delete a node in the middle 
#(i.e., any node but the first and last node, not necessarily the exact middle) 
#of a singly linked list, given only access to that node.


from random import randrange


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


def remNode (h: SLinkedList, n: Node):
    i = h.headval
    p = h.headval
    while (i != None):
        if (i == n):
            p.nextval = i.nextval
        p = i
        i = i.nextval

#Better solution
def remNodeV2 (n: Node):
    n.dataval = n.nextval.dataval
    n.nextval = n.nextval.nextval

list1 = SLinkedList()
list1.headval = Node(1)
it = list1.headval

#generate linked list
for i in range(10):
    n = Node (randrange(10))
    it.nextval = n
    it = it.nextval

it = list1.headval
s = ""
while (it != None):
    s += str((it.dataval)) + ", "
    it = it.nextval
print(s)

print(list1.headval.nextval.nextval.nextval.dataval)

remNodeV2(list1.headval.nextval.nextval.nextval)

it = list1.headval
s = ""
while (it != None):
    s += str((it.dataval)) + ", "
    it = it.nextval
print(s)