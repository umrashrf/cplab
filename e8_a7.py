import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	c = 1
	for a in range(0, 9):
		for b in range(8, a, -1):
			sys.stdout.write(" ")
		
		sys.stdout.write("%.lf" % c * c)
		sys.stdout.write("\n")
		c = c * 10 + 1

	getch()
	
if __name__ == "__main__":
	main()