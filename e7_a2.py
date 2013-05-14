from os import system
from math import pow

from helpers.getch import getch

def main():
	system("clear")
	
	print("Equation: 3 x^4 + 4 x^3 + x^2 + 7x + 9")
	print("\n")

	x = float(raw_input('Write value of X: '))

	answer = 0
	answer += 3 * pow(x, 4)
	answer += 4 * pow(x, 3)
	answer += pow(x, 2)
	answer += 7 * x
	answer += 9
	
	print("\n")
	print("Answer: %f" % answer)

	getch()
	
if __name__ == "__main__":
	main()