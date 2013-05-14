import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	for a in range(4):
		b = 0
		while b <= 3:
			sys.stdout.write("%d%d\t" % (a, b))
			b += 1
		sys.stdout.write("\n")

	getch()
	
if __name__ == "__main__":
	main()