from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	arr = [0, 0, 0, 0, 0]
	
	for a1 in range(1, 5):

		for a2 in range(5, 0, -1):
			arr[a1] = arr[a2 - 1]

		arr[0] = int(raw_input("Enter value for FILO "))
		print(" ".join(map(str, arr)))
		getch()
		system("clear")
	
	print(" ".join(map(str, arr)))
	getch()
	
if __name__ == "__main__":
	main()