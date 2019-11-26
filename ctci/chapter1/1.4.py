#1.4
#Palindrome Permutation

def permutPalindrome(s: str):
    #assume utf-8
    b = [0] * 128
    for c in s:
        b[ord(c)]+=1
    single = False
    for val in b:
        if (val % 2 == 1):
            if (single):
                return False
            single = True
    return True

Tests = ['asdf', 'TEEst', '', '1fdas@34', 'abc', 'aabbccdde']

for s in Tests:
    print(permutPalindrome(s))
