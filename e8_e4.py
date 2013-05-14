from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = 0
	while a <= 3:
		b = 0
		while b <= 3:
			print("%d%d\t" % (a, b))
			b += 1
		print("\n")
		a += 1

	getch()
	
if __name__ == "__main__":
	main()