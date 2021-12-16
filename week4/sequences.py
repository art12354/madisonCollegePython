#1
varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]
#2
print(varString[3:])
print(varString[:3])
print(varString[3:12])
print(varString[::2])
print(varString[::-1])
#3
print(varList[::-1])
print(varList[2::-1])
print(varList[2:4])
print(varList[::3])
print(varList[1:])
for letter in varString:
    print(letter)
for word in varList:
    print(word)
