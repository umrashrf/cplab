import sys
from os import system
from helpers.getch import getch
from helpers.getche import getche

def main():
	system("clear")

	nm1 = nm2 = 1.0

	while not (nm1 == 0.0 and nm2 == 0.0):
		exp = raw_input("Type Number Operator Number\n").split()
		nm1, op, nm2 = float(exp[0]), int(exp[1]), float(exp[2])
		if op == 1:
			sys.stdout.write(" = %f" % (nm1 + nm2))
		elif op == 2:
			sys.stdout.write(" = %f" % (nm1 - nm2))
		print("\n\n")
	getch()
	
if __name__ == "__main__":
	main()