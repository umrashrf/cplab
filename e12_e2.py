from os import system
from helpers.getch import getch

def main():
	system("clear")
	add1(2, 4)	
	getch()

def add1(a, b):
	print("\n%d + %d = %d" % (a, b, a + b))

if __name__ == "__main__":
	main()