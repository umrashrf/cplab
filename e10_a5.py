'''
CGPA and Percentage NOT DONE YET
'''
import sys
from os import system
from helpers.getch import getch
from helpers.getche import getche

def main():
	system("clear")

	print("You will be asked to enter marks in 0 - 100 range.\n")
	
	math = raw_input("Enter Math Marks: ")
	print(get_grade(int(math)) + "\n")
	
	physics = raw_input("Enter Physics Marks: ")
	print(get_grade(int(physics)) + "\n")

	electronics = raw_input("Enter Electronics Marks: ")
	print(get_grade(int(electronics)) + "\n")

	islamiat = raw_input("Enter Islamiat Marks: ")
	print(get_grade(int(islamiat)) + "\n")

	programming = raw_input("Enter Programming Marks: ")
	print(get_grade(int(programming)) + "\n")

	getch()
	
def get_grade(marks):
	if marks < 0 and marks > 100:
		return "Marks out of range"

	if marks >= 0 and marks < 50:
		return "Grade F"

	if marks >= 50 and marks < 60:
		return "Grade C"

	if marks >= 60 and marks < 70:
		return "Grade C+"

	if marks >= 70 and marks < 80:
		return "Grade B"

	if marks >= 80 and marks < 90:
		return "Grade B+"

	if marks >= 90 and marks < 95:
		return "Grade A"

	if marks >= 96 and marks <= 100:
		return "Grade A+"

if __name__ == "__main__":
	main()