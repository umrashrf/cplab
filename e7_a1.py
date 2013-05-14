from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	distance = float(raw_input("Enter distance in kilometers: "))
	print("Distance in meters: %f" % (distance * 1000))
	
	getch()
	
if __name__ == "__main__":
	main()