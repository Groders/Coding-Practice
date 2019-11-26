#1.5
#One Away: There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away. 

def oneAway(s1: str, s2: str):

    if (len(s1) == 1 and len(s2) == 0 or len(s2) == 1 and len(s1) == 0 ):
        return True
    #swap a char
    if (len(s1) == len(s2)):
        diff = False
        for a,b in zip(s1, s2):
            if (a != b):
                if (diff == True):
                    return False
                diff = True
        return True
    #add a char
    elif (len(s1) - len(s2) == -1):
        found = 0
        for i in range(len(s1)):
            if (s1[i] != s2[i + found]):
                if (found == 0 and s1[i] == s2[i + 1]):
                    found = 1
                else:
                    return False
        return True
    #rem char
    elif (len(s1) - len(s2) == 1):
        found = 0
        for i in range(len(s2)):
            if (s1[i] != s2[i - found]):
                if (found == 0 and s1[i + 1] == s2[i]):
                    found = 1
                else:
                    return False
        return True
    else:
        return False

Tests = [("test", "tes"), ("test", "test"), ("", " "), ("test", "tes"), ("asdf", "sdf"), ("qsdf", "aqdf")]

for test in Tests:
    print(oneAway(test[0],test[1]))
