# guess_hard version
# 產生一個隨機整數1~100(不用印出來)
# 讓使用者重複輸入數字去猜 > 迴圈
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他比答案大/小

import random

r = random.randint(1, 100)
cont = 0
while True:
	num = input("猜一個數字: ")
	num = int(num)
	cont += 1
	if num == r:
		print("終於猜對了!")
		print('猜了', cont, "次")
		break
	elif num > r:
		print("太大了!再猜")
	else:
		print("太小了!再猜")
	print('猜了', cont, "次")