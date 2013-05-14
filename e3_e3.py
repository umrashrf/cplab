from os import system
from helpers.getch import getch

def main():
	system("clear")
	print("\n%d" % ord('a'))
	print("\n%s" % "Iqra University")
	print("\n%c" % chr(20))
	print("\n%f" % 35.5)
	print("\n%ld" % 1234567)
	getch()
	
if __name__ == "__main__":
	main()