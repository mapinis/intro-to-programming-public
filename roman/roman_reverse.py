inp = input("Input roman numerals: ").upper() + " "
tot = 0

numeralDict = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

inp = list(inp)
for charNum in range(len(inp)):
    char = inp[charNum]
    if(char == "I"):
        if(inp[charNum + 1] != "I" and inp[charNum + 1] != " "):
            tot -= 1
        else:
            tot += 1
    elif(char != " "):
        tot += numeralDict[char]

print(tot)