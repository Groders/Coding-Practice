#1.2
#Check Permutation: Given two strings, write a method to decide if one is a permutation of the
#other. 

#strip whitespace
#check len
#check same number of chars 
def isPermutation(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if (len(s1) != len(s2)):
        return False
    
    #assume utf-8
    b1 = [0] * 128
    b2 = [0] * 128
    for i, j in zip(s1, s2):
        b1[ord(i)] += 1
        b2[ord(j)] += 1

    for i, j in zip(b1, b2):
        if (i != j):
            return False
    return True


Tests = [("test", "estt"), ("qwerty", "asdf"), ("", " "), ("1w2e", "1 2 w e")]

for test in Tests:
    print(isPermutation(test[0], test[1]))