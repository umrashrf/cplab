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
	dob = raw_input("\nDate of Birth			:	dd-mm-yyyy\n")
	dob = map(int, dob.split("-"))
	print("%d-%d-%d" % (dob[0], dob[1], dob[2])) # reading string but converting to int
	print("\nAddress				:	%s" % "PIDC, Karachi")
	phone = raw_input("\nCell Phone			:	(3XX-XXXXXXX)\n")
	phone = map(int, phone.split("-"))
	print("0%d-%ld" % (phone[0], phone[1]))
	cnic = raw_input("\nCNIC				:	(12345-1234567-1)\n")
	cnic = map(int, cnic.split("-"))
	print("%d-%ld-%d" % (cnic[0], cnic[1], cnic[2]))
	print("\nGender				:	%s" % "Male")
	print("\nHSC (College/Board)		:	%s" % "Bahria College, M.T. Khan Road")
	print("\nHSC Year			:	%d" % 2008)
	print("\nSSC (School/Board)		:	%s" % "J.M.A School Karachi")
	print("\nHSC Year			:	%d" % 2006)
	getch()
	
if __name__ == "__main__":
	main()