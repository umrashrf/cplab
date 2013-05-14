from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 5
	print("\n%d %d %d" % (a - 5, a - 1, a))
	print("\n%d" % a)

	getch()
	
if __name__ == "__main__":
	main()