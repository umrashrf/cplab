import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")

	cp = int(raw_input("Enter CP marks between 1 and 100\n"))
	if cp >= 0 and cp <= 100:
		if cp >= 75:
			print("Grade A")
		else:
			if cp >= 50:
				print("Grade C")
	else:
		print("Incorrect Input")

	getch()
	
if __name__ == "__main__":
	main()