import sys
from getch import getch

def getche():
	i = getch()
	sys.stdout.write(i)
	return i