# -*- coding:utf-8 -*-
#解析對話紀錄格式

def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	
	A_word_count  = 0
	V_word_count  = 0

	A_sticker_count  = 0
	V_sticker_count  = 0

	A_image_count = 0
	V_image_count = 0	

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]

		if name == 'Allen':
			if s[2] == '貼圖':
				A_sticker_count += 1
			elif s[2] == '圖片':
				A_image_count += 1
			else:
				for m in s[2:]:
					A_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				V_sticker_count += 1
			elif s[2] == '圖片':
				V_image_count += 1
			else:
				for m in s[2:]:
					V_word_count += len(m)
			
	print('Allen說了', A_word_count, '傳了', A_sticker_count, '個貼圖', '傳了', A_image_count, '個圖片')
	print('Viki說了', V_word_count, '傳了', V_sticker_count, '個貼圖', '傳了', V_image_count, '個圖片')		

def write_file(file_name, lines):
	with open(file_name, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('out.txt', lines)

main()