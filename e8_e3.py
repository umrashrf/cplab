from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 0
	while 0:
		print("%d x 2 = %d\n" % (a, a * 2))
		a += 1

	getch()
	
if __name__ == "__main__":
	main()