import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	for a in range(1, 10, 2):
		for b in range(9, a, -2):
			sys.stdout.write(" ")

		for c in range(1, a + 1):
			sys.stdout.write("+")

		sys.stdout.write("\n")
	
	getch()
	
if __name__ == "__main__":
	main()