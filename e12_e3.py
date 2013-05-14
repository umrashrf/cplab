from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 2
	b = 4
	c1 = add1(2, 4)	
	print("\n%d + %d = %d" % (a, b, c1))

	getch()

def add1(a, b):
	c2 = a + b
	return c2
	
if __name__ == "__main__":
	main()