#1.7
#Rotate Matrix: Given an image represented by an NxN matrix, 
#where each pixel in the image is 4 bytes, write a method to 
#rotate the image by 90 degrees. can you do this in place?
from typing import List

#question was for bytes, but we can ignore that :)
def rotateMatrix(m: List[List[bytes]]) -> List[List[bytes]]:
    n = len(m)//2
    l = len(m) -1
    for i in range(0, n):
        for j in range(i, l - i):
            temp = m[i][j]
            m[i][j] = m[j][l-i] 
            m[j][l-i] = m[l-i][l-j] 
            m[l-i][l-j] = m[l-j][i] 
            m[l-j][i] = temp


    return m




a = [0] * 5

for i in range(len(a)):
    a[i] = [0] * 5
    for j in range(len(a[i])):
        a[i][j] = (i * j)

for line in a:
    print(line)
print("\n")
for line in rotateMatrix(a):
    print(line)