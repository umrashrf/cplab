from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	dd = 11
	mm = 11
	yyyy = 1989
	cell1 = 300
	cell2 = 1234567
	cnic1 = 12345
	cnic2 = 1234567
	cnic3 = 1

	print("\n******************************RESUME******************************")
	print("\n********************************CV********************************")
	print("\n******************************************************************")
	print("\n==================================================================")
	print("\nName				:	%s" % "Umair")
	print("\nFathers Name			:	%s" % "Ashraf")
	print("\nDate of Birth			:	%d-%d-%d" % (dd, mm, yyyy))
	print("\nAddress				:	%s" % "PIDC, Karachi")
	print("\nCell Phone			:	0%d-%ld" % (cell1, cell2))
	print("\nCNIC				:	%d-%ld-%d" % (cnic1, cnic2, cnic3))
	print("\nGender				:	%s" % "Male")
	print("\nHSC (College/Board)		:	%s" % "Bahria College, M.T. Khan Road")
	print("\nHSC Year			:	%d" % 2008)
	print("\nSSC (School/Board)		:	%s" % "J.M.A School Karachi")
	print("\nHSC Year			:	%d" % 2006)
	getch()
	
if __name__ == "__main__":
	main()