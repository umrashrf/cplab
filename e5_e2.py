from os import system
from math import sin, cos, tan, sinh, cosh, tanh, pow, sqrt

from helpers.getch import getch

def main():
	system("clear")
	
	print("\n\n\n Trignometric Functions")
	print("\nsin 45 = %.2f" % sin(45))
	print("\ncos 45 = %.2f" % cos(45))
	print("\ntan 45 = %.2f" % tan(45))

	print("\n\n\n Hyperbolic Functions")
	print("\nsinh 1 = %.2f" % sinh(1))
	print("\ncosh 1 = %.2f" % cosh(1))
	print("\ntanh 1 = %.2f" % tanh(1))

	print("\n\n\n Math Functions")
	print("\npow 2,3 = %.2f" % pow(2, 3))
	print("\nsqrt 49 = %.2f" % sqrt(49))

	getch()
	
if __name__ == "__main__":
	main()