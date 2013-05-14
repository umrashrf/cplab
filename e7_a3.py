from os import system

from helpers.getch import getch

def main():
	system("clear")
	
	x = int(raw_input('Enter a number: '))
	print("Answer: %d" % (x * x))

	getch()
	
if __name__ == "__main__":
	main()