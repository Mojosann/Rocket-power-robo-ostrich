# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
handle = open(name, 'r')

mail_dict = {}
for line in handle:
    if line.startswith('From '):
	line = line.strip('\n')
	mail = line.split(' ')[1]
	#print(mail)
	count = 0
	if mail_dict.get(mail) == None:
	     mail_dict[mail] = 1
	else:
	     mail_dict[mail] = mail_dict[mail]+1
			
#max_sending = max([mail_dict[mail] for mail in mail_dict])
for key, value in mail_dict.items():
    if value == max(mail_dict.values()):
        max_key = key
print(max_key, mail_dict[max_key])
