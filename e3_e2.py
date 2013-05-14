from os import system
from helpers.getch import getch

def main():
	system("clear")
	print("\n%c %s %d %f %ld" % ('a', "Iqra University", 20, 35.5, 1234567))
	getch()
	
if __name__ == "__main__":
	main()