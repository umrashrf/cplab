from os import system
from helpers.getch import getch

def main():
	system("clear")
	print("\n%c" % 'a')
	print("\n%s" % "Iqra University")
	print("\n%d" % 20)
	print("\n%f" % 35.5)
	print("\n%ld" % 1234567)
	getch()
	
if __name__ == "__main__":
	main()