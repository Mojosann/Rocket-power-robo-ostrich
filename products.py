# -*- coding:utf-8 -*-
# 製作商品 / 價格清單

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

#印出清單內的小清單
for p in products:
	#print(p)
	print(p[0], '的價格是', p[1]) #印出名稱

#csv是一種蠻常被用來儲存資料的檔案格式可以用excel打開
#csv用','可以分欄
#with的功能可以自動close		    #加入編碼修正檔案內有編碼的問題
with open ('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n') #加入欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
							#將p[1]轉回為字串才能與+做合併