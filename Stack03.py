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
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, char):
        self.stack.append(char)

    def pop(self):
        return self.stack.pop()