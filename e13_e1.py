from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	aa = ["Engineering", "Department", "Iqra", "University", "Karachi"]
	for a in aa:
		print(a)

	getch()
	
if __name__ == "__main__":
	main()