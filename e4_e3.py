from os import system
from helpers.getch import getch

def main():
	system("clear")
	a = chr(97)
	b = ord('A')
	c = 12.5
	d = 1234567
	print("%c %d %f %lf" % (a, b, c, d))
	getch()
	
if __name__ == "__main__":
	main()