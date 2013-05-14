from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 2
	b = 4
	c1 = c2 = c3 = c4 = 5
	d1 = d2 = d3 = d4 = 8

	print("\n%d %d %d %d" % (a + b, a - b, a * b, a / b))
	print("\n%d %d %d %d %d %d" % (a > b, a < b, a >= b, a <= b, a == b, a != b))
	print("\n%d %d %d %d" % (c1 + 3, c2 - 3, c3 * 3, c4 / 3))
	print("\n%d %d %d %d" % (d1 + 1, d2 + 1, d3 - 1, d4 - 1))

	getch()
	
if __name__ == "__main__":
	main()