from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	aaa = [
		[[1, 2], [3, 4], [5, 6]],
		[[7, 8], [9, 10], [11, 12]],
		[[13, 14], [15, 16], [17, 18]],
		[[19, 20], [21, 22], [23, 24]]
	]
	print("%d" % aaa[2][1][0])

	getch()
	
if __name__ == "__main__":
	main()