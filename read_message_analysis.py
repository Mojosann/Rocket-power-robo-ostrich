#新增使用套件效果(缺點：cmd要全寬不然會顯示有誤)
import time, progressbar

#篩選資料範例
data = []
cont = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		cont += 1 
		bar.update(cont)
print('檔案讀取完了, 總共有', len(data), '筆資料') #有幾筆資料


#取留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	avg = sum_len / len(data)
print("留言的平均長度為", avg)


#撈出留言長度比100小的
new = []
for d in data: #讀取原本資料
	if len(d) < 100:
		new.append(d) #裝進新的清單
print('一共有', len(new), '筆留言小於100')
#print(new[0])
#print(new[1]) 


#撈出幾筆資料提到good
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言說讚')
#print(good[0]) 印出第一筆含有good的留言

#list comprehension的寫法
good = [d for d in data if 'good' in d]


#文字計數
start_tim = time.time()
wc = {} #word_count dict
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_tim, 'seconds.')


#print(len(wc)) 一百萬筆留言總長度
#print(wc['Allen']) 這個key出現次數
	

#設計查詢留言內出現過的字有幾次
while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過!')
print('感謝使用本查詢功能')
