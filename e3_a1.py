from os import system
from helpers.getch import getch

def main():
	system("clear")
	print("\n******************************RESUME******************************")
	print("\n********************************CV********************************")
	print("\n******************************************************************")
	print("\n==================================================================")
	print("\nName				:	%s" % "Umair")
	print("\nFathers Name			:	%s" % "Ashraf")
	print("\nDate of Birth			:	%d-%d-%d" % (15, 01, 1989))
	print("\nAddress				:	%s" % "PIDC, Karachi")
	print("\nCell Phone			:	0%d-%ld" % (300, 1234567))
	print("\nCNIC				:	%d-%ld-%d" % (12345, 1234567, 1))
	print("\nGender				:	%s" % "Male")
	print("\nHSC (College/Board)		:	%s" % "Bahria College, M.T. Khan Road")
	print("\nHSC Year			:	%d" % 2008)
	print("\nSSC (School/Board)		:	%s" % "J.M.A School Karachi")
	print("\nHSC Year			:	%d" % 2006)
	getch()
	
if __name__ == "__main__":
	main()