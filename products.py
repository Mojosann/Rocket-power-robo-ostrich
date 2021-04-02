# -*- coding:utf-8 -*-
# 製作商品 / 價格清單

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

#印出清單內的小清單
for p in products:
	#print(p)
	print(p[0], '的價格是', p[1]) #印出名稱