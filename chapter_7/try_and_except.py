#!/usr/bin/python3

if __name__ == "__main__":
	input_num = input("Enter a number between 0 and 10: ")
	try:
		val = int(input_num)
		if val > 0 and val < 10: 
			print("The value is valid")
	except ValueError as error: 
		print(error)