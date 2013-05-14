'''
NOT DONE YET
'''

import sys
from os import system
from helpers.getch import getch

def main():
	system("clear")

	print("Think of a number between 1 and 99")
	print("Press 'g' for greater")
	print("Press 'l' for less")
	print("Press 'e' for equal\n")

	incr = gss = 50
	while incr > 1.0:
		print("Is your number greater, less or equal to %.0f" % gss)
		incr /= 2
		ch = getch()
		if ch == 'e':
			break
		elif ch == 'g':
			gss += incr
		else:
			gss -= incr

	print("You guessed %.0f" % gss)
	
	getch()
	
if __name__ == "__main__":
	main()