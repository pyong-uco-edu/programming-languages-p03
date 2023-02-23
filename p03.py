# -------------------------------------------------------------
# Team Identification Block
# Author 1:	            	Lisa Sun
# Student ID:	            *20300925
# E-Mail:		            lsun1@uco.edu
# Student 1 CRN:           	22142, Spring 2023
# Author 2:	            	Philip Yong
# Student ID:	            *20512220
# E-Mail:		            pyong@uco.edu
# Student 2 CRN:	        21502, Spring 2023
# Course:		            CMSC 4023 - Programming Languages
# Project:	 	            p03
# Due:		 	            March 20, 2023
# Project Account Number:	tt048
# --------------------------------------------------------------
import sys
from Stack03 import Stack

stack = Stack()
infile = ""
outfile = ""

# Get Args
if len(sys.argv) > 3:
    print(
        "Too many arguments. Only accepting 0, 1 or 2 args. You put in", len(sys.argv), "args.")
    exit()

if len(sys.argv) == 1:
    infile = input("Enter the input file name: ")
    outfile = input("Enter the output file name: ")

if len(sys.argv) == 2:
    infile = sys.argv[1]
    outfile = input("Enter the output file name: ")

if len(sys.argv) == 3:
    infile = sys.argv[1]
    outfile = sys.argv[2]


# Read File
infile = open(infile, "r")
outfile = open(outfile, "w")
line = infile.readline()
isBalanced = True

while line != "":
    # Read Chars
    for letter in line:
        # Check for Left
        if letter == '(' or letter == '[' or letter == '{':
            stack.push(letter)
            # print("push: " + letter)
        # Check for Right
        elif letter == ')' or letter == ']' or letter == '}':
            poppedChar = stack.pop()
            # print("match: " + letter)
            # print("pop: " + poppedChar)
            if poppedChar != "(" and letter == ")":
                # print(poppedChar + " " + letter)
                isBalanced = False
            if poppedChar != "[" and letter == "]":
                # print(poppedChar + " " + letter)
                isBalanced = False
            if poppedChar != "{" and letter == "}":
                # print(poppedChar + " " + letter)
                isBalanced = False

    # Write what is Read
    outfile.write("%s" % (line))
    line = infile.readline()

# Output Results
if isBalanced:
    outfile.write("%s" % (" is balanced."))
else:
    outfile.write("%s" % (" is not balanced."))

outfile.close()
infile.close()
