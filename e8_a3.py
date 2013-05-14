import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	for a in range(3, -1, -1):
		for b in range(3, -1, -1):
			sys.stdout.write("%d%d\t" % (a, b))
		sys.stdout.write("\n")
	
	getch()
	
if __name__ == "__main__":
	main()