from os import system
from math import sin, cos, tan, sinh, cosh, tanh

from helpers.getch import getch

def main():
	system("clear")
	
	a = 45
	b = 1

	sn = sin(a)
	cs = cos(a)
	tn = tan(a)
	
	snh = sinh(b)
	csh = cosh(b)
	tnh = tanh(b)

	print("\n\n\n Trignometric Functions")
	print("\nsin 45 = %.2f" % sn)
	print("\ncos 45 = %.2f" % cs)
	print("\ntan 45 = %.2f" % tn)

	print("\n\n\n Hyperbolic Functions")
	print("\nsinh 1 = %.2f" % snh)
	print("\ncosh 1 = %.2f" % csh)
	print("\ntanh 1 = %.2f" % tnh)

	getch()
	
if __name__ == "__main__":
	main()