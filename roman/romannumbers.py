#####################
# Name: Dr. Hickman
# Date: 02/13/17, Class Comparison
# File: romannumbers.py
# Description: Code to convert a decimal number from 1 to 3999 to
# Roman numerals. This code corresponds to problem 3
########################

from sys import exit

## A function that converts a decimal value (1s, 10s, 100s)
# to the appropriate Roman numeral sequence.
# @param num, The whole value to be converted.
# @param placeHolder, The decimal place (1, 10, 100) that is being converted.
# @return, Type <str> sequence of Roman numerals
#
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

sInput = input("ROMAN NUMBER CONVERTER\nEnter a value from 1 to 3999: ")

# Check for valid input 
if (not sInput.isdigit()) :
    print("The input is an invalid data type (letters)")
    exit()  # Exit program on invalid input
else:
    x = int(sInput)
    if (x <=0 or x > MAX_VALUE) :
        print("The input is an invalid data type (number)")
        exit()  # Exit program on invalid input

year = int(sInput) #If validation is passed, convert the input to an integer
romanStr = ""  # Initialize an empty string variable

romanStr = (year // 1000) * "M"  # Convert the thousands first

n = year % 1000  # Calculate the remainder after thousands
romanStr = romanStr + convertNum(n, 100)  # Concatenate the hundreds to the string

n = n % 100  # Calculate the remainder after hundreds
romanStr = romanStr + convertNum(n, 10)  # Concatenate the tens to the string

n = n % 10   # Calculate the remainder after tens
romanStr = romanStr + convertNum(n, 1)  # Concatenate the ones to the string

print("\nThe year converted to Roman numbers is: ", romanStr)  # Output result
