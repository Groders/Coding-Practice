#1.7
#Rotate Matrix: Given an image represented by an NxN matrix, 
#where each pixel in the image is 4 bytes, write a method to 
#rotate the image by 90 degrees. can you do this in place?
from typing import List

#question was for bytes, but we can ignore that :)
def rotateMatrix(m: List[List[bytes]]) -> List[List[bytes]]:
    n = len(m)//2
    l = len(m)
    for i in range(n):
        for j in range(n):
            temp = m[i][j]
            m[i][j] = m[j][l-1-i] 
            m[j][l-1-i] = m[l-1-i][l-1-j] 
            m[l-1-i][l-1-j] = m[l-1-j][i] 
            m[l-1-j][i] = temp
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