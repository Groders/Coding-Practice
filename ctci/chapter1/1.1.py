#1.1
#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures? 
import sys 
def isUnique(s: str):
    #assume utf-8
    if (len(s) > 128):
        return False
    checker = [False] * 128
    for c in s:
        if checker[ord(c)]:
            return False
        checker[ord(c)] = True
    return True

Tests = ['asdf', 'TEEst', '', '1fdas@34', 'a'*128]

for s in Tests:
    print(isUnique(s))