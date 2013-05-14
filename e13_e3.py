from os import system
from helpers.getch import getch

def main():
	system("clear")
	
	a = [8, 6, 3, 7, 2]
	
	print(" ".join(map(str, a)))
	vl = raw_input("From the above enter one value to search: ")
	vl = int(vl)

	a2 = 0
	while a[a2] != vl:
		a2 += 1

	print("Location of %d is %d" % (vl, a2 + 1))

	getch()
	
if __name__ == "__main__":
	main()