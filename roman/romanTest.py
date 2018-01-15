f = open("romanTest.txt", 'w')

numeralArr = [
    (1000, "M"),
    (500, "D"),
    (100, "C"),
    (50, "L"),
    (10, "X"),
    (5, "V"),
    (1, "I")]

out = ""

def convert(num, nums, iters, halfs):
    global out    
    if num >= nums[0] - iters[0]:
        out += iters[1] + nums[1]
        num -= nums[0] - iters[0]
    elif num < nums[0] - iters[0]:
        if halfs[0]: out += halfs[2];  num -= halfs[1]
        out += iters[1] * (num // iters[0])
        num -= iters[0] * (num // iters[0])
    elif num == nums[0]:
        out += nums[1]
        num -= nums[0]
    return num

for userNum in range(1, 5000):
    preserveNum = userNum
    out = ""
    for x in range(0, len(numeralArr) - 2, 2):
        number, numeral = numeralArr[x]
        halfNumber, halfNumeral = numeralArr[x + 1]
        iterNumber, iterNumeral = numeralArr[x + 2]
        out += numeral * (userNum // number)
        userNum -= number * (userNum // number)
        userNum  = convert(userNum, (number, numeral) if userNum >= halfNumber else (halfNumber, halfNumeral), (iterNumber, iterNumeral), [userNum >= halfNumber, halfNumber, halfNumeral])
    f.write(str(preserveNum) + "  " + out + "\n")

f.close()

numerals = open("numerals.txt")
romans = open("romanTest.txt")

nums = numerals.readlines()
roms = romans.readlines()

for x in range(len(nums)):
    num = nums[x]
    rom = roms[x]
    if(num != rom): print(num, rom, sep="")