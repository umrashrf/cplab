from random import randint
from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = []
	for b in range(10):
		a.append(randint(1, 100))
		print("\n%d" % a[b])
	
	getch()
	
if __name__ == "__main__":
	main()