from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	arr = [23, 16, 97, 33, 42]

	for a in range(5):
		for b in range(4):
			if arr[b] > arr[b + 1]:
				tmp = arr[b]
				arr[b] = arr[b + 1]
				arr[b + 1] = tmp
				
	print(" ".join(map(str, arr)))
	getch()
	
if __name__ == "__main__":
	main()