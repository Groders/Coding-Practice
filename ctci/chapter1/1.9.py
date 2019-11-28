#1.9
#String Rotation: Assume you have amethod isSubstring which checks 
#ifone word is asubstring of another. Given two strings, s1 and s2, 
#write code to check if s2 is a rotation of s1 using only one call to 
#isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").

#in keyword is bascially substring
def isRotation(s1: str, s2: str) -> bool:
    if (len(s1) != len(s2)):
        return False
    s = s1*2
    if s2 in s:
        return True
    return False


s1 = "waterbottle"
s2 = "erbottlewat"

print(isUnisSubstring(s1,s2))