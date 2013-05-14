from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	x = int(raw_input("Enter a number: "))

	answer = 1
	for i in range(x):
		answer *= (i + 1)

	print("Factorial of %d is %d" % (x, answer))

	getch()
	
if __name__ == "__main__":
	main()