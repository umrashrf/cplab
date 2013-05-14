import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 0
	while a <= 3:	
		for b in range(4):
			sys.stdout.write("%d%d\t" % (a, b))
		sys.stdout.write("\n")
		a += 1
		
	getch()
	
if __name__ == "__main__":
	main()