import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")

	chrs = raw_input("Type any sentence ")
	print("Total Characters = %d" % len(chrs))
	print("Total word = %d" % len(chrs.split()))

	getch()
	
if __name__ == "__main__":
	main()