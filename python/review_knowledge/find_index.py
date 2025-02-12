# find the which index for letters
def findOccurence(s):
    a = s.find("b")
    b = s.find("c")
    return a, b

print(findOccurence("aaabbbccc"))