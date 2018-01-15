f = open("romanTest.txt", 'w')
out = ""

def convertNum(num, placeHolder):
    if (placeHolder == 100):       # if table to reference which Roman
        r1 = "C"                   # numerals are needed for the conversion
        r5 = "D"
        r10 = "M"
    elif (placeHolder == 10):
        r1 = "X"
        r5 = "L"
        r10 = "C"
    else:
        r1 = "I"
        r5 = "V"
        r10 = "X"       
    howMany = num // placeHolder
    if (howMany <= 3):       # if table to find the Roman numeral pattern
        return howMany * r1
    elif (howMany == 4):
        return r1 + r5
    elif (howMany == 5):
        return r5
    elif (howMany == 9):
        return r1 + r10
    else:
        return r5 + (howMany -5) * r1

## MAIN BODY PROGRAM ##

MAX_VALUE = 3999  # Constant for the maximum conversion value

for sInput in range(1, 4999):
    year = int(sInput) #If validation is passed, convert the input to an integer
    romanStr = ""  # Initialize an empty string variable

    romanStr = (year // 1000) * "M"  # Convert the thousands first

    n = year % 1000  # Calculate the remainder after thousands
    romanStr = romanStr + convertNum(n, 100)  # Concatenate the hundreds to the string

    n = n % 100  # Calculate the remainder after hundreds
    romanStr = romanStr + convertNum(n, 10)  # Concatenate the tens to the string

    n = n % 10   # Calculate the remainder after tens
    romanStr = romanStr + convertNum(n, 1)  # Concatenate the ones to the string

    f.write(str(sInput) + "  " + romanStr + "\n")

f.close()

numerals = open("numerals.txt")
romans = open("romanTest.txt")

nums = numerals.readlines()
roms = romans.readlines()

for x in range(len(roms)):
    num = nums[x]
    rom = roms[x]
    if(num != rom): print(num, rom, sep="")