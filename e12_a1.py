import sys
from os import system
from helpers.getch import getch
from helpers.getche import getche

def main():
	system("clear")
	resume()
	getch()

def resume():
	print("\n******************************RESUME******************************")
	print("\n********************************CV********************************")
	print("\n******************************************************************")
	print("\n==================================================================")
	sys.stdout.write("\nName				:	")
	ch = ord(getche())
	while (ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122) or (ch == ' ') or ch != 13:
		ch = ord(getche())
	
	sys.stdout.write("\nFathers Name			:	")
	while getche() != '\r':
		pass
	dob = raw_input("\nDate of Birth			:	dd-mm-yyyy\n")
	dob = map(int, dob.split("-"))
	print("%d-%d-%d" % (dob[0], dob[1], dob[2])) # reading string but converting to int
	sys.stdout.write("\nAddress				:	")
	while getche() != '\r':
		pass
	phone = raw_input("\nCell Phone			:	(3XX-XXXXXXX)\n")
	phone = map(int, phone.split("-"))
	print("0%d-%ld" % (phone[0], phone[1]))
	cnic = raw_input("\nCNIC				:	(12345-1234567-1)\n")
	cnic = map(int, cnic.split("-"))
	print("%d-%ld-%d" % (cnic[0], cnic[1], cnic[2]))
	sys.stdout.write("\nGender				:	")
	while getche() != '\r':
		pass
	sys.stdout.write("\nHSC (College/Board)		:	")
	while getche() != '\r':
		pass
	print("\nHSC Year			:	%d" % 2008)
	sys.stdout.write("\nSSC (School/Board)		:	")
	while getche() != '\r':
		pass
	print("\nHSC Year			:	%d" % 2006)

if __name__ == "__main__":
	main()