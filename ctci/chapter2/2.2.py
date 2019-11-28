#2.2
#Return Kth to Last: Implement an algorithm 
#to find the kth to last element of a singly linked list.

#assuming no cycles

from random import randrange

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


def kthLast (h: SLinkedList, k: int):

    v = None
    
    def iterator (n: Node):
        nonlocal v
        if (n == None):
            return 0
        else:
            count = iterator(n.nextval)
            if (count == k):
                v = n.dataval
            return count + 1
    

    iterator(h.headval)
    return v



            
list1 = SLinkedList()
list1.headval = Node(1)
it = list1.headval

for i in range(20):
    n = Node (randrange(20))
    it.nextval = n
    it = it.nextval


it = list1.headval
s = ""
while (it != None):
    s += str((it.dataval)) + ", "
    it = it.nextval
print(s)

print(kthLast(list1, 10))