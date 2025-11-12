str = "label"
newStr = []
for c in str:
    print(ord(c) ^ 13)
    newStr.append(ord(c) ^ 13)

for c in newStr:
    
    print(chr(c))

# print(newStr)