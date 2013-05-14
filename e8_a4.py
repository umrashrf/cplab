import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	for a in range(4):
		for b in range(4):
			sys.stdout.write("%d%d\t" % (a, b))
		sys.stdout.write("\n")
	
	getch()
	
if __name__ == "__main__":
	main()