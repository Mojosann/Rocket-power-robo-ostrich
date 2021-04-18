# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')

for line in fh:
	data = line.strip('\n')
	uppercase = data.upper()
	print(uppercase)
