#1.8
#Zero Matrix: Write an algorithm such that if 
#an element in an MxN matrix is 0, its entire row and column are set to O.

def zeroMatrix(m):
    if (len(m) == 0 or len(m[0]) == 0):
        return m

    h = [False] * len(m)
    w = [False] * len(m[0])

    for i, col in enumerate (m):
        for j, ele in enumerate (col): 
            if (ele == 0):
                h[i] = True
                w[j] = True

    for i in range(len(m)):
        for j in range(len(m[0])):
            if (h[i] == True or w[j] == True):
                m[i][j] = 0

    return m


a = [0] * 5

for i in range(len(a)):
    a[i] = [0] * 5
    for j in range(len(a[i])):
        a[i][j] = (i + j)

for line in a:
    print(line)
print("\n")
for line in zeroMatrix(a):
    print(line)