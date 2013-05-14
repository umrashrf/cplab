import sys
from os import system
from helpers.getch import getch
from helpers.getche import getche

def main():
	system("clear")

	sys.stdout.write("Name: ")
	ch = ''
	while ch != '\r':
		ch = ord(getche()) 
		if (ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122) or (ch == ''):
			pass
		else:
			sys.stdout.write('\b \b')
		ch = chr(ch)

	getch()
	
if __name__ == "__main__":
	main()