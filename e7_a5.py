from os import system

from helpers.getch import getch

def main():
	system("clear")

	i = 1000
	count = 0
	a = int(raw_input('Enter 4 digit number: '))
	
	while a > 0:
		count += a / i
		a = a % i
		i /= 10
		
	print("Total: %d" % count)

	getch()
	
if __name__ == "__main__":
	main()