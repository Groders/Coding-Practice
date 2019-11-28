#2.6
#Palindrome: Implement a function to check if a linked list is a palindrome.

#assuming no cycles

from random import randrange
from collections import deque

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

    def isPalindrome(self):
        q = deque()
        def iterator (n: Node):
            nonlocal q
            if (n == None):
                return True
            else:
                q.append(n.dataval)
                rtn = iterator(n.nextval)
                val = q.popleft()
                if (val != n.dataval):
                    rtn = False
                return rtn

        return iterator(self.headval)

list1 = SLinkedList.genList(randrange(10), 10)
list1.printList()

list2 = SLinkedList()
list2.headval = Node(1)
it = list2.headval
it.nextval = Node(2)
it.nextval.nextval = Node(1)

list2.printList()

print(list1.isPalindrome())
print(list2.isPalindrome())