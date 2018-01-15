#####################
# Name: Mark Apinis
# Date: 2-13-17
# File: roman.py
# Description: Converts numbers to roman numerals
########################

userNum = int(input("Input a number: "))                                                        # User inputs a number
out = ""                                                                                        # Declaration of out, which will be the output

numeralArr = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")]    # Array that holds number -> numeral data

## Convert, converts the given number as far as it can into roman numerals in steps of numerals
#  @param num (int), the number that the user inputs, or what remains of it after running through convert
#  @param nums (int, string), the number and numeral that make up the current use
#  @param iters (int, string), the number and numeral of the iteration numeral, which is always 2 after the current
#  @param halfs [bool, int, string], the number and numeral of the halfway between the current and 0, bool decides if needs to be used
#  @return num (int), the damaged userNum, as well as adds numerals to out
def convert(num, nums, iters, halfs):
    global out                                                                                  # Assures that global out is added to

    if num >= nums[0] - iters[0]:                                                               # Decides if the number is in the top section, like CD < num < D
        out += iters[1] + nums[1]                                                               # Adds the iterator and the numeral to out
        num -= nums[0] - iters[0]                                                               # Removes the value of the above numerals from num
            
    elif num < nums[0] - iters[0]:                                                              # Decides if the number is not in the top, like num < CD
        if halfs[0]: out += halfs[2];  num -= halfs[1]                                          # Decides if it is in the upper half of the current num, then makes sure that the num changes reflect that

        out += iters[1] * (num // iters[0])                                                     # Adds the iterators for the amount left, like XX
        num -= iters[0] * (num // iters[0])                                                     # Removes the value of the above numerals from num

    elif num == nums[0]:                                                                        # Decides if the number is exactly the highest possible num, like D
        out += nums[1]                                                                          # Adds the numeral to out
        num -= nums[0]                                                                          # Removes the value of the aboce addition

    return num                                                                                  # Returns the changed userNum

for x in range(0, len(numeralArr), 2):                                                          # Iterates through the numerals 2 at a time
    number, numeral = numeralArr[x]                                                             # Assigns the current number and numeral

    if x < len(numeralArr) - 1: halfNumber, halfNumeral = numeralArr[x + 1]                     # Assigns current halfNumber and halfNumeral, makes sure there are no out of bounds
    else: halfNumber, halfNumeral = -1, ""

    if x < len(numeralArr) - 2: iterNumber, iterNumeral = numeralArr[x + 2]                     # Assigns current iterNumber and iterNumeral, makes sure there are no out of bounds
    else: iterNumber, iterNumeral = -1, ""

    out += numeral * (userNum // number)                                                        # If the usernum is larger than the num, it adds those numerals
    userNum -= number * (userNum // number)                                                     # Removes the above numerals from the num
    
    userNum  = convert(userNum,                                                                 # Assigns userNum to convert output, passes userNum
        (number, numeral) if userNum >= halfNumber else (halfNumber, halfNumeral),               # If it is the upper half of the selectior (like num > 500), then it is true, and passes nums
        (iterNumber, iterNumeral),                                                              # Passes the iterators
        [userNum >= halfNumber, halfNumber, halfNumeral])                                        # Sends the halfs, first one depends if it is upper half 

print(out)                                                                                      # Output of out