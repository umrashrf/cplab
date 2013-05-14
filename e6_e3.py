import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	sys.stdout.write("What is your section : ")
	sys.stdout.write(getch())
	print('')
	
	getch()
	
if __name__ == "__main__":
	main()