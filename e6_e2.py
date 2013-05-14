from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a, b, c, d = raw_input("Enter char integer float double ").split()
	b = int(b)
	c = float(c)
	d = float(d)

	print("\n%c %d %f %lf" % (a, b, c, d))
	
	getch()
	
if __name__ == "__main__":
	main()