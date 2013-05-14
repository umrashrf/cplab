import sys
from os import system
from helpers.getch import getch
from helpers.getche import getche

def main():
	system("clear")

	nm1 = nm2 = 1.0

	while not (nm1 == 0.0 and nm2 == 0.0):
		exp = raw_input("Type Number Operator Number\n").split()
		nm1, ch, nm2 = float(exp[0]), exp[1], float(exp[2])
		if ch == '+':
			sys.stdout.write(" = %f" % (nm1 + nm2))
		elif ch == '-':
			sys.stdout.write(" = %f" % (nm1 - nm2))
		elif ch == '*':
			sys.stdout.write(" = %f" % (nm1 * nm2))
		elif ch == '/':
			sys.stdout.write(" = %f" % (nm1 / nm2))
		print("\n\n")
	getch()
	
if __name__ == "__main__":
	main()