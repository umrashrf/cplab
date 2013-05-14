from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = raw_input("Enter character ")
	b = int(raw_input("Enter integer "))
	c = float(raw_input("Enter float "))
	d = float(raw_input("Enter double ")) # float is double of C
	
	print("\n%c %d %f %lf" % (a, b, c, d))
	
	getch()
	
if __name__ == "__main__":
	main()