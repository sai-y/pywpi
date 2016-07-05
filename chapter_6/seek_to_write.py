#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 

	file = open('write_file.txt', 'w')
	
	# read the second line from the file 
	file.seek(53)
	
	data = file.write('Hello')
	print(data)
	file.close()