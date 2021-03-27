# guess_讓使用者產生一個隨機整數
# 讓使用者重複輸入數字去猜 > 迴圈
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他比答案大/小

import random
start = input('請決定隨機數字範圍開始值: ')
start = int(start)
end = input('請決定隨機數字範圍結束值: ')
end = int(end)

r = random.randint(start, end)
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