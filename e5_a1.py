from os import system
from math import sin, cos, tan, sinh, cosh, tanh, pow, sqrt

from helpers.getch import getch

def main():
	system("clear")
	
	print("Equation: 3 x^4 Sin(180x) + 4 x^3 cos(90x) + x^2 sin(tan(45)) + 7x + 9 cos(90 x^2)")
	print("\n")

	x = float(raw_input('Write value of X: '))

	answer = 0
	answer += 3 * pow(x, 4) * sin(180 * x)
	answer += 4 * pow(x, 3) * cos(90 * x)
	answer += pow(x, 2) * sin(tan(45))
	answer += 7 * x
	answer += 9 * cos(90 * pow(x, 2))
	
	print("\n")
	print("Answer: %f" % answer)

	getch()
	
if __name__ == "__main__":
	main()