from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 'a'
	a1 = 'b'
	
	b = 12
	b1 = 13
	
	c = 12.5
	c1 = 13.5
	
	d = 1234567
	d1 = 1234568
	
	print("%c %d %f %lf" % (a, b, c, d))
	print("%c %d %f %lf" % (a1, b1, c1, d1))
	
	getch()
	
if __name__ == "__main__":
	main()