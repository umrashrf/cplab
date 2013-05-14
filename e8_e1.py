from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	for a in range(13):
		print("%d x 2 = %d\n" % (a, a * 2))
	
	getch()
	
if __name__ == "__main__":
	main()