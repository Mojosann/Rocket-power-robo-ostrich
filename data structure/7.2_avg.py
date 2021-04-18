# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
for line in fh:
	if line.startswith("X-DSPAM-Confidence:"): 
		data = line.strip('\n')
		num = float(data.split(' ')[1])
		count += num
		avg = count / (len(data)+1)
print('Average spam confidence:', avg)
