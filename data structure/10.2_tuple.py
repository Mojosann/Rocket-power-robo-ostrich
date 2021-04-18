# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
handle = open(name)

hour_dict = {}
for line in handle:
  if line.startswith('From '):
    line = line.strip('\n')
		hour = line.split(' ')[6][0:2]
		#print(hour)
		count = 0
		if hour_dict.get(hour) == None:
			hour_dict[hour] = 1
		else:
			hour_dict[hour] = hour_dict[hour]+1
            
for hout, times in sorted(hour_dict.items()):
	print(hout, times)
