from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	for a in range(10, 22, 2):
		print("%d x 2 = %d" % (a, a * 2))
	
	getch()
	
if __name__ == "__main__":
	main()